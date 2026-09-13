# LeetCode 489: Robot Room Cleaner — Building the Thought Process from Zero

## The real interview goal

This problem looks unusual because I cannot see the room and cannot directly choose a grid cell.
I only control a robot through four operations:

```text
move forward
turn left
turn right
clean the current cell
```

The interview goal is not to instantly remember a special robot trick. It is to reduce the
unfamiliar interface to a familiar idea:

```text
unknown room
    -> discover reachable cells as I move
    -> treat each open cell as a graph node
    -> run DFS on that implicit graph
    -> physically undo every recursive move
    -> restore both position and direction
```

The transferable lesson is:

> When recursion changes real or simulated state, backtracking must restore all of that state,
> not just the part that is easiest to notice.

Here, the state is `(position, direction)`, even though direction is not part of the visited key.

---

## Step 1: Strip away the story

An accessible cell is connected to each accessible neighbor in the four cardinal directions.
That is an unweighted graph:

- each open cell is a node;
- an edge exists between two adjacent open cells;
- walls simply mean that an edge does not exist.

The room is hidden, but DFS does not require the whole graph up front. It only needs a way to ask:

```text
Can I enter this neighboring node?
```

`robot.move()` answers exactly that question while also moving the robot when the answer is yes.

So I can restate the problem:

> Explore every node reachable from the starting node in an implicit graph, and clean each node.

This immediately suggests DFS or BFS. DFS is the more natural fit because its recursive return
already describes the physical behavior I need: enter a neighbor, explore it, then come back.

### What I would say aloud

> “I do not know the room layout, but I can discover it online. I will assign my own coordinates
> to cells relative to the start and perform DFS over the reachable cells.”

---

## Step 2: Invent coordinates even though the robot has none

The API does not expose the robot's row or column. That does not prevent me from maintaining a
logical coordinate system.

Choose the starting cell as:

```text
(0, 0)
```

Then define directions consistently, for example:

```cpp
// up, right, down, left
vector<pair<int, int>> dirs = {
    {-1, 0}, {0, 1}, {1, 0}, {0, -1}
};
```

The coordinates do not need to match the room's real coordinates. They only need to be internally
consistent. If I move up from logical `(r, c)`, I call the new cell `(r - 1, c)`.

Now I can maintain a visited set of logical coordinates and avoid cycles.

### Why a visited set is essential

A room can contain cycles:

```text
A -- B
|    |
D -- C
```

Without `visited`, DFS can keep walking around the cycle forever. Cleaning a cell is not a safe
replacement for `visited` because the interface gives me no way to ask whether a cell is already
clean.

### The modeling distinction

My logical state and the robot's physical state are different but synchronized:

```text
logical state:  (row, col, direction) in my DFS parameters
physical state: robot's actual cell and orientation in the hidden room
```

Every command must preserve agreement between the two.

---

## Step 3: Start with ordinary DFS pseudocode

If I had a visible grid, I would write:

```text
dfs(cell):
    mark cell visited
    clean cell

    for each of four neighboring cells:
        if neighbor is unvisited and open:
            dfs(neighbor)
```

With the robot API, “neighbor is open” becomes `robot.move()`.

A first draft might therefore be:

```text
dfs(current cell):
    mark and clean current cell

    for each direction:
        face that direction
        if target coordinate is unvisited and move() succeeds:
            dfs(target)
```

This is close, but it contains the problem's main trap.

After the recursive call finishes, where is the physical robot?

Unless the child explicitly walks back, the robot is still somewhere inside the child's subtree.
The parent's logical variables say it is at the parent, but the real robot is not. From that point
on, all computed coordinates are wrong.

That question reveals the need for physical backtracking.

---

## Step 4: Derive the `goBack` operation

Suppose the robot moved from parent `P` into child `C` while facing toward `C`:

```text
P  -->  C
```

When `dfs(C)` finishes, I want the robot to be back at `P`, facing the same direction it faced
when it entered `C`.

The API has no “move backward,” so simulate it:

```text
turn 180 degrees
move forward once
turn 180 degrees again
```

In code:

```cpp
void goBack(Robot& robot) {
    robot.turnRight();
    robot.turnRight();
    robot.move();
    robot.turnRight();
    robot.turnRight();
}
```

The first two turns face the parent. The move returns to the parent. The last two turns restore the
original orientation.

The final two turns may look unnecessary, but they are crucial. Position alone is not the complete
physical state.

### The DFS contract

Before writing more code, state a precise invariant:

> `dfs(robot, r, c, d)` begins with the robot physically at logical cell `(r, c)`, facing direction
> `d`. It ends with the robot at the same cell, facing the same direction.

This contract makes recursive reasoning manageable. A caller can explore a child without needing
to know anything about what happened inside the child.

---

## Step 5: Handle direction without getting lost

Use direction indices in clockwise order:

```text
0 = up
1 = right
2 = down
3 = left
```

Then one right turn changes direction `d` to:

```text
(d + 1) % 4
```

During one DFS call, try all four directions. A clean pattern is:

```cpp
for (int i = 0; i < 4; ++i) {
    int nextDir = (dir + i) % 4;
    // The robot is currently facing nextDir.

    ... possibly explore the cell ahead ...

    robot.turnRight(); // prepare for the next iteration
}
```

Why is the robot facing `nextDir` at the start of every iteration?

- On the first iteration, it still faces the direction passed into this DFS call.
- If a move fails, it remains facing the attempted direction, then turns right once.
- If a recursive exploration succeeds, `goBack` restores its direction, then it turns right once.

After four right turns, it returns to the original direction. Thus the DFS contract holds.

This is easier to trust than trying to reason about turns locally. The invariant explains the
whole loop.

---

## Step 6: Decide exactly when to mark a cell visited

For the coordinate in front of the robot:

```text
if already visited:
    do not move into it
else if move() succeeds:
    mark it visited
    recurse
    go back
```

Mark the cell before recursion, not after. This is the standard DFS rule that prevents another
path in a cycle from entering the same node while it is still being explored.

Do not mark a coordinate merely because `move()` failed. A failed move means that coordinate is a
wall relative to the chosen logical map. Remembering walls is optional; remembering visited open
cells is sufficient for the required bounds.

The starting cell must also be marked before the first DFS call.

---

## Step 7: Put the reasoning into code

Here is a canonical implementation whose loop matches the invariant directly:

```cpp
class Solution {
private:
    set<pair<int, int>> visited;
    const vector<pair<int, int>> dirs{
        {-1, 0}, {0, 1}, {1, 0}, {0, -1}
    };

    void goBack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }

    void dfs(Robot& robot, int row, int col, int dir) {
        visited.insert({row, col});
        robot.clean();

        for (int i = 0; i < 4; ++i) {
            int nextDir = (dir + i) % 4;
            int nextRow = row + dirs[nextDir].first;
            int nextCol = col + dirs[nextDir].second;

            if (!visited.count({nextRow, nextCol}) && robot.move()) {
                dfs(robot, nextRow, nextCol, nextDir);
                goBack(robot);
            }

            robot.turnRight();
        }
    }

public:
    void cleanRoom(Robot& robot) {
        dfs(robot, 0, 0, 0);
    }
};
```

It does not matter which absolute direction the robot initially faces. I simply name its initial
direction `0`; all logical coordinates are relative to that choice.

---

## How the repository solution differs

The existing solution uses:

```cpp
for (int kk = 1; kk <= 4; ++kk) {
    robot.turnRight();
    int nxtDir = (curDir + kk) % 4;
    ...
}
```

So it turns before trying a direction rather than after. Its exploration order is:

```text
right, backward, left, original direction
```

instead of:

```text
original direction, right, backward, left
```

Both orders are correct. The important relationship is that the physical turn and the logical
direction update occur together.

Its inline backtracking sequence:

```cpp
robot.turnRight();
robot.turnRight();
robot.move();
robot.turnRight();
robot.turnRight();
```

is exactly `goBack`. Extracting it into a named helper usually makes the interview explanation
clearer and reduces the chance of omitting a turn.

The repository solution stores coordinates as strings such as `"2#-1"`. That works, but
`set<pair<int, int>>` or `unordered_set` with a pair hash expresses the intent more directly and
avoids string construction. This is a representation choice, not an algorithmic difference.

---

## A small execution trace

Suppose the start cell `A` has an open cell `B` to its right.

```text
A B
```

Assume DFS at `A` is facing up.

```text
1. Clean A.
2. Try up; move fails. Turn right.
3. Now face right; B is unvisited and move succeeds.
4. Recurse at B, recording B's logical coordinate and direction.
5. DFS(B) explores everything reachable through B.
6. DFS(B) finishes at B with the same direction it had on entry.
7. goBack(): turn around, move to A, turn around again.
8. The robot is at A facing right, exactly as before recursion.
9. Turn right and continue with A's next direction.
```

Notice that the recursive call returning in the programming language does not physically return
the robot. `goBack` is what makes the physical world match the call stack.

---

## Correctness argument

An interview proof can be organized around three claims.

### 1. Every cleaned coordinate is a reachable open cell

The start is reachable. Every other DFS call happens only after `robot.move()` succeeds from a
reachable cell, so that cell is also open and reachable.

### 2. Every reachable open cell is eventually visited

At each visited cell, DFS physically attempts all four directions. Whenever an adjacent cell is
open and unvisited, `move()` succeeds and DFS visits it. Therefore no reachable neighbor is missed.
By graph reachability, no cell in the connected component of the start is missed.

### 3. Every reachable cell is cleaned exactly once

A coordinate is marked visited before its DFS call, so cycles cannot cause another DFS call for
the same coordinate. Each DFS call cleans its current cell once. Combined with claim 2, every
reachable cell is cleaned exactly once.

The state-restoration invariant ensures that after each child exploration, the parent continues
from the correct physical cell and direction, so all four of its neighbors are tested correctly.

---

## Complexity

Let `N` be the number of reachable open cells.

- Time: `O(N)`. Each reachable cell is visited once and considers four directions. Robot commands
  per direction are constant, so the total is linear in `N`.
- Space: `O(N)` for the visited set and up to `O(N)` recursion depth in the worst case.

Some blocked locations may be attempted from neighboring cells, but each visited cell makes only
four directional checks, so this does not change the `O(N)` bound.

---

## Common wrong turns and how to recover

### “I need the room dimensions first”

I do not. This is an implicit graph. DFS discovers neighbors through `move()` and stops at walls.

Recovery question:

> “Can I explore a graph without constructing all of it first?”

Yes—this is the same idea used for generated states in many search problems.

### “The API gives no coordinates, so I cannot use visited”

Coordinates can be relative. Assign `(0, 0)` to the start and update the coordinates according to
my own direction convention.

Recovery question:

> “Do I need globally true coordinates, or only stable unique labels for cells?”

Only stable labels are needed.

### Forgetting to move back after recursion

Then the call stack says “I returned to the parent,” but the robot remains in the child subtree.
Logical and physical state diverge.

Recovery question:

> “What physical state did this recursive call mutate, and how will I undo it?”

### Moving back but not restoring direction

Turning 180 degrees and moving restores the cell but leaves the robot facing backward. Subsequent
logical direction calculations no longer match reality.

Recovery question:

> “What must be identical before and after a DFS call?”

Answer: both position and direction.

### Turning only after a successful move

The robot must advance to the next direction whether the current direction is blocked, already
visited, or successfully explored. Put the one right turn at a common point in the loop.

### Calling `move()` before checking `visited`

This can physically enter an already visited cell. It can still be repaired by immediately backing
out, but it adds commands and makes the invariant harder to maintain. Compute the logical target
and check `visited` first.

### Using BFS without planning physical navigation

BFS can organize logical nodes in a queue, but the one physical robot cannot teleport from one
queued node to the next. I would need to store and replay routes between cells. DFS naturally keeps
the current physical route on the call stack, which is why it is the simpler choice.

---

## What I would say in an interview

A concise progression could sound like this:

> “I can model every open cell as a node and successful moves as edges. Although the robot does not
> expose coordinates, I can assign relative coordinates starting from `(0, 0)` and use those in a
> visited set. I will run DFS because after exploring a neighboring cell I can physically retrace
> that one edge to return to the parent.”

Then identify the subtle part:

> “My DFS invariant is that a call returns with the robot at the same cell and facing the same
> direction as when the call began. After recursion, I turn 180 degrees, move once, and turn 180
> degrees again. That restores both position and orientation.”

Then finish with mechanics and complexity:

> “At each cell I clean once, try all four directions, and rotate right after each attempt. The
> visited set prevents cycles. If `N` cells are reachable, the time and auxiliary space are both
> `O(N)`.”

This explanation exposes the model, invariant, implementation, and proof before getting buried in
turn arithmetic.

---

## A reusable checklist for similar problems

When I see an unfamiliar control interface or hidden environment:

1. **Identify the graph.** What are the nodes, and what operation reveals an edge?
2. **Create my own labels.** Can relative coordinates or generated IDs represent hidden states?
3. **Track all mutable state.** Is it position only, or also direction, inventory, switches, etc.?
4. **State the recursive contract.** What must be true when the call begins and when it returns?
5. **Build an undo operation.** How do I reverse a successful transition?
6. **Mark before exploring.** Prevent cycles as soon as a state is discovered.
7. **Check synchronization.** Do my logical variables still match the external system after every
   branch?

The deepest pattern is not robot-specific:

```text
choose
    -> mutate state
    -> recurse
    -> undo the mutation completely
```

That is the essence of backtracking.

---

## Final mental model

Keep two pictures in mind at the same time:

```text
Logical DFS                         Physical robot
-----------                         --------------
coordinate (r, c)       <------->   current cell
direction d             <------->   current orientation
recurse to neighbor     <------->   move forward
return to parent        <------->   turn around, move, turn around
visited set             <------->   memory of discovered open cells
```

DFS decides **where to explore**. `goBack` guarantees the robot is physically in the correct place
to continue exploring. The solution works only because those two views remain synchronized.
