# Cracking the safe
* [De Bruijn sequence](https://en.wikipedia.org/wiki/De_Bruijn_sequence)

## Translated problem statement
* Find the shortest string that contains every possible length-n string over the digits 0 ... k-1 as a consecutive substring.

## minimum length -> shortest distance -> BFS
## Model the graph
## last N digits -> sliding window

## ChatGpt - Thought Process

> The standard spelling is **De Bruijn sequence**. The central idea is: represent every
> length-`n` password as an **edge**, then find an Eulerian circuit that uses every edge once.

## 1. Strip away the story

The safe checks the most recent `n` digits after every digit we type. Therefore, typing one
string succeeds for every possible password exactly when:

> Every length-`n` string over the alphabet `0 ... k - 1` occurs somewhere as a consecutive
> substring.

There are `k^n` possible passwords. So the problem is really:

> Construct the shortest string containing all `k^n` possible length-`n` strings as windows.

This is the definition of a linearized **De Bruijn sequence**.

## 2. Get a lower bound before designing an algorithm

A string of length `L` has only

```text
L - n + 1
```

windows of length `n`.

We need at least `k^n` distinct windows, so:

```text
L - n + 1 >= k^n
L >= k^n + n - 1
```

This tells us exactly what an optimal construction must do:

- begin with one window of length `n`;
- make every additional digit create one new password;
- never waste a window by repeating a password before all passwords have been used.

That lower bound is an important habit. It changes the question from “How can I find a short
string?” to “Can I build a string that meets this exact bound?”

## 3. Focus on how consecutive windows overlap

Suppose the current window is:

```text
a1 a2 ... an
```

After appending digit `x`, the next window is:

```text
a2 a3 ... an x
```

The two windows overlap in exactly `n - 1` digits. That overlap is the state we need to
remember.

This suggests the graph:

- **Vertex:** a string of length `n - 1`.
- **Directed edge:** a string of length `n` (one possible password).
- For password `s`, the edge goes from `s[0:n-1]` to `s[1:n]`.
- The edge can be labeled with the final digit of `s`.

For example, with `n = 3`, the password `012` is the edge:

```text
01 --append 2--> 12
```

Walking across that edge means typing `2` while the current suffix is `01`, which creates the
new length-3 window `012`.

## 4. Decide whether the required objects are vertices or edges

This is the recognition step that unlocks the problem.

We must include every **password** once. In this graph, passwords are **edges**, not vertices.
Therefore we need a walk that uses every edge exactly once: an **Eulerian circuit**.

This also explains why the tempting BFS thought is not right:

- BFS answers shortest-path or minimum-number-of-steps-to-a-destination questions.
- Here there is no single destination and no choice to skip required passwords.
- We must cover every required object while maximizing overlap between consecutive objects.
- “Use every edge exactly once” points to Euler, not BFS.

It is possible to make each complete password a vertex and connect compatible passwords. That
turns the problem into a Hamiltonian-path-looking problem (“visit every vertex once”), which is
usually much harder. Choosing length-`n - 1` overlaps as vertices makes the special structure
visible and turns the passwords into edges.

### Reusable modeling rule

When strings must be chained using a fixed overlap:

1. Make the overlap the vertex.
2. Make each required string/piece an edge.
3. Ask whether the problem is an Eulerian trail or circuit.

This same model appears in reconstructing a string from fixed-length fragments (`k`-mers),
assembling sequences from overlaps, and arranging directed pairs so every pair is used once.

## 5. Why an Eulerian circuit is guaranteed to exist

For every vertex of length `n - 1`:

- there are `k` outgoing edges, one for each digit we can append;
- there are `k` incoming edges, one for each digit that could precede it.

Therefore every vertex has:

```text
indegree = outdegree = k
```

The graph is also connected in the directed sense needed here. From any vertex, we can reach
any target vertex by appending the target's digits one at a time; after `n - 1` appends, the
current suffix is the target.

Balanced degrees plus connectivity gives us an Eulerian circuit.

## 6. Use Hierholzer's algorithm, not ordinary DFS output

Hierholzer's algorithm constructs an Eulerian circuit:

1. Start at any vertex, such as `'0' * (n - 1)`.
2. Follow an unused outgoing edge.
3. Mark **the edge** as used.
4. Continue from the edge's destination.
5. Add the edge's digit to the answer only after exploring the destination.

The last point is the subtle one. A greedy walk can enter a dead end while unused edges remain
elsewhere. Postorder records a completed local circuit and splices it into the larger circuit.
That is the core idea of Hierholzer's algorithm.

The DFS records edge labels in reverse Eulerian order, so reverse those labels at the end and
place them after the starting `(n - 1)`-digit vertex.

## 7. Derive the implementation from the model

```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)
        used_edges = set()
        reversed_edge_labels = []

        def visit(node: str) -> None:
            for digit in map(str, range(k)):
                edge = node + digit       # one length-n password
                if edge in used_edges:
                    continue

                used_edges.add(edge)
                next_node = edge[1:]       # keep the last n-1 digits
                visit(next_node)
                reversed_edge_labels.append(digit)

        visit(start)
        return start + "".join(reversed(reversed_edge_labels))
```

How each line maps back to the graph:

- `node` is the current `(n - 1)`-digit suffix.
- `edge = node + digit` is a complete length-`n` password.
- `used_edges` prevents a password from being used twice.
- `edge[1:]` is the next overlap state.
- appending after recursion is Hierholzer postorder.
- the initial `start` supplies the first `n - 1` digits; every traversed edge supplies one more.

For `n = 1`, `start` is the empty string, there is one empty vertex, and the `k` digits are
self-loop edges. The same model and code still work.

## 8. Small example: `n = 2`, `k = 2`

Passwords:

```text
00, 01, 10, 11
```

Vertices are one-digit overlaps: `0` and `1`.

```text
00: 0 -> 0
01: 0 -> 1
10: 1 -> 0
11: 1 -> 1
```

One Eulerian circuit uses the edges in this order:

```text
00, 01, 11, 10
```

Start with vertex `0`, then append the label contributed by each edge:

```text
0 + 0 + 1 + 1 + 0 = 00110
```

Its length-2 windows are:

```text
00, 01, 11, 10
```

All four passwords appear, and the length is:

```text
k^n + n - 1 = 2^2 + 2 - 1 = 5
```

So it meets the lower bound and is optimal.

## 9. Correctness proof to reproduce in an interview

### Every possible password appears

Each length-`n` password corresponds to exactly one graph edge. Hierholzer's algorithm traverses
every edge exactly once. Writing the starting vertex followed by the traversed edge labels makes
each traversed edge appear as one consecutive length-`n` window. Therefore every password
appears exactly once as a window.

### The returned string is shortest

There are `k^n` passwords. A length-`L` string contains at most `L - n + 1` length-`n` windows,
so any valid answer needs `L >= k^n + n - 1`. The construction contains an initial `n - 1`
digits plus one digit for each of the `k^n` edges, for total length `k^n + n - 1`. It reaches
the lower bound, so it is shortest.

## 10. Complexity

There are:

```text
k^(n - 1) vertices
k^n edges
```

Every edge is processed once.

- Time: `O(k^n * n)` with string slicing/hashing as written.
- Space: `O(k^n * n)` for stored string edges, plus the traversal stack.

With integer-encoded states, the factor from string construction can be reduced, but the string
version exposes the mental model more clearly and is usually the best version to derive first.

One language-specific caution: recursive Hierholzer can have a call stack proportional to the
number of edges. If the environment has a low recursion limit, use an explicit stack or an
integer-state iterative version. This does not change the graph model.

## 11. Common wrong turns and what they teach

### “Minimum length means BFS”

Optimization words alone do not choose the algorithm. First determine what a state, move, and
required object are. BFS minimizes the number of edges between endpoints; it does not solve an
“include every edge” requirement.

### Marking vertices as visited

The same `(n - 1)` suffix must be revisited many times through different passwords. Marking a
vertex visited would incorrectly discard valid edges. Track used **edges**.

### Greedily appending digits and returning the current string

A local choice may close a small cycle or hit a temporary dead end. Hierholzer fixes this by
recording edges in postorder, after the continuation is exhausted.

### Treating each password as a vertex

That hides the overlap structure and suggests visiting every vertex once. Moving the overlap
into the vertices transforms required passwords into edges and reveals an Eulerian problem.

### Proving only that the construction works

A valid sequence is not automatically shortest. Pair the construction with the window-count
lower bound, then show that their lengths match.

## 12. Recognition checklist for future problems

Ask these questions in order:

1. Can I restate the story as “contain/use every fixed-length object”?
2. How do two consecutive objects overlap?
3. Is that overlap the smallest sufficient state?
4. Should required objects be modeled as edges rather than vertices?
5. Does the task say every edge must be used exactly once?
6. Do all vertices have balanced indegree and outdegree?
7. Is the relevant part of the graph connected?
8. If yes, can Hierholzer construct the Eulerian trail/circuit?
9. What counting lower bound proves optimality?

A compact memory hook:

> Fixed-length pieces + maximum suffix/prefix overlap + use every piece = overlap vertices,
> piece edges, Eulerian traversal.

## 13. Boundary of this technique

This approach is especially clean because the problem contains **all** length-`n` strings, so
the overlap graph is balanced and connected.

If a problem gives only an arbitrary subset of fragments:

- the same graph model may still apply;
- check Euler-trail degree conditions (`out - in` values) and connectivity;
- an Eulerian trail may have different start and end vertices.

If fragments have different lengths or may be reused/omitted, the problem may instead resemble
shortest common superstring, dynamic programming, or another optimization problem. Do not apply
the De Bruijn/Euler pattern solely because the statement mentions substrings; the fixed overlap
and “use each required piece as an edge” structure are the decisive clues.
