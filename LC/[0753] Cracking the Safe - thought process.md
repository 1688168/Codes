# LeetCode 753: Cracking the Safe — Building the Thought Process from Zero

## The real interview goal

If I have never seen De Bruijn sequences, I should not expect myself to jump directly from the
safe story to “Eulerian circuit.” That leap is pattern recognition learned after solving the
problem.

The interview skill I can reproduce is a chain of smaller deductions:

```text
simulate the mechanism
    -> rewrite it as substring coverage
    -> establish a minimum possible length
    -> experiment with a tiny case
    -> identify the overlap that determines the next state
    -> model each password as a transition
    -> realize every transition must be used once
    -> apply or derive an Eulerian traversal
```

The important lesson is not “memorize De Bruijn sequence.” It is:

> When fixed-length objects can overlap, make the overlap the state and make each required
> object a transition.

---

## Step 1: Make sure I understand what the safe actually does

The safe does not wait for me to submit one complete password. After every digit I type, it
checks the most recent `n` digits.

For example, if `n = 3` and I type:

```text
0 1 2 0 3
```

the safe checks these length-3 windows:

```text
012, 120, 203
```

Therefore, one typed string is guaranteed to open the safe if every possible length-`n`
password occurs as one of its windows.

I can now discard the safe story and restate the problem:

> Find the shortest string that contains every length-`n` string over digits `0 ... k - 1`
> as a substring.

This restatement is already major progress. It tells the interviewer that I understand the
mechanics even if I do not yet know the algorithm.

### What I would say aloud

> “Each new digit creates one new length-`n` window. So I want one string whose windows cover
> all `k^n` possible passwords.”

---

## Step 2: Find a lower bound before searching for an algorithm

There are `k^n` possible passwords.

A typed string of length `L` contains:

```text
L - n + 1
```

length-`n` windows. Therefore:

```text
L - n + 1 >= k^n
L >= k^n + n - 1
```

So no answer can be shorter than `k^n + n - 1`.

This gives me a concrete target. An optimal construction must arrange things so that every new
digit contributes a previously unseen password window. There can be no wasted window.

### Why this helps my thinking

Without the lower bound, “shortest string” may make me reach vaguely for BFS or dynamic
programming. The lower bound reveals the real challenge:

> Can I order all passwords so consecutive passwords reuse `n - 1` digits?

That is an overlap/ordering question, not a shortest-path question.

---

## Step 3: Work the smallest nontrivial example by hand

Take:

```text
n = 2, k = 2
digits = {0, 1}
passwords = {00, 01, 10, 11}
```

Naively concatenating the passwords produces:

```text
00011011
```

but this is far longer than the lower bound:

```text
2^2 + 2 - 1 = 5
```

Can I reach length 5? One answer is:

```text
00110
```

Its windows are:

```text
00, 01, 11, 10
```

What made this work?

```text
00 -> 01  because the first ends in 0 and the second starts with 0
01 -> 11  because the first ends in 1 and the second starts with 1
11 -> 10  because the first ends in 1 and the second starts with 1
```

Consecutive length-2 passwords share one digit. In general, consecutive length-`n` passwords
should share `n - 1` digits.

### The question that moves me forward

> “What part of the current password determines which password can come next?”

Only its last `n - 1` digits matter.

---

## Step 4: Choose the smallest sufficient state

Suppose the current length-`n` window is:

```text
a1 a2 ... an
```

If I append digit `x`, the next window becomes:

```text
a2 a3 ... an x
```

To know my possible next moves, I do not need the whole string typed so far. I only need:

```text
a2 a3 ... an
```

the final `n - 1` digits.

So my state is:

> the current suffix of length `n - 1`.

From a suffix, I can append any digit from `0` through `k - 1`. Appending one digit creates one
complete password.

For example, when `n = 3`:

```text
current suffix = 01
append 2
new password = 012
next suffix = 12
```

I can draw this as a directed transition:

```text
01 --[password 012 / append 2]--> 12
```

Now the graph model has emerged naturally:

- a vertex is an `(n - 1)`-digit suffix;
- an edge is an `n`-digit password;
- traversing the edge means appending its last digit;
- the destination is the new `(n - 1)`-digit suffix.

I did not have to know the final graph in advance. I got it by asking for the smallest information
needed to determine the next move.

---

## Step 5: Ask what exactly must be visited

This distinction is often the decisive graph-modeling question:

> Are the required objects vertices or edges?

The problem requires me to include every password. In my graph, every password is an edge.
Therefore I need to use every edge.

To achieve the lower bound, I must use every edge exactly once.

That sentence is the Eulerian-circuit signal:

> Find a walk that traverses every edge exactly once.

If I remember graph terminology, I now say “Eulerian trail/circuit.” If I do not remember the
name, I can still describe exactly what traversal I need.

### Why not make passwords the vertices?

I could make every length-`n` password a vertex and connect two vertices when they overlap. Then
I would need to visit every vertex once, which looks like a Hamiltonian-path problem.

That model is valid but unhelpful. Hamiltonian problems are generally hard. Using the overlap as
the vertex and the required pieces as edges exposes a much easier Eulerian structure.

### Reusable modeling lesson

When I must arrange overlapping pieces:

```text
overlap/context = vertex
required piece = edge
using a piece = traversing its edge
```

---

## Step 6: Verify that an Eulerian circuit should exist

I should not merely name an algorithm. I need to verify its conditions.

For any `(n - 1)`-digit vertex:

- I can append any of `k` digits, so it has `k` outgoing edges.
- Any of `k` digits could have preceded it, so it has `k` incoming edges.

Thus every vertex has:

```text
indegree = outdegree = k
```

The graph is also connected in the required directed sense. To move from any suffix to a target
suffix, append the target suffix's digits one at a time. After `n - 1` appends, the current suffix
is the target.

So the graph is balanced and connected. It has an Eulerian circuit.

### What I would say aloud

> “Each suffix has `k` ways to enter and `k` ways to leave, and all suffixes are mutually
> reachable by appending digits. So an Eulerian circuit exists.”

---

## Step 7: What if I remember Euler but not Hierholzer's algorithm?

Start with the obvious attempt:

```text
From the current suffix, choose an unused password edge and continue.
```

The danger is that I may exhaust the outgoing edges of my current vertex while unused edges
remain elsewhere. Returning the path immediately in forward order can lock in the wrong local
choice.

The repair is to use DFS and add an edge to the result only after exploring everything reachable
through that edge:

```text
visit(node):
    for every digit:
        edge = node + digit
        if edge is unused:
            mark edge used
            visit(edge's suffix)
            record digit
```

Why record on the way back?

When a vertex has no unused outgoing edge, I know its position at the end of the remaining local
route is settled. Postorder lets smaller closed tours be spliced into the larger tour. This is
the mechanism behind Hierholzer's algorithm.

The recorded edges are in reverse traversal order, so reverse them at the end.

---

## Step 8: Derive the code line by line

```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)
        used = set()
        reverse_labels = []

        def dfs(suffix: str) -> None:
            for digit in map(str, range(k)):
                password = suffix + digit
                if password in used:
                    continue

                used.add(password)
                next_suffix = password[1:]
                dfs(next_suffix)
                reverse_labels.append(digit)

        dfs(start)
        return start + "".join(reversed(reverse_labels))
```

The code is easier to remember when every variable has a graph meaning:

```text
suffix             = current vertex
password           = directed edge
used               = edges already traversed
password[1:]       = destination vertex
append after dfs   = Hierholzer postorder
```

The returned string consists of:

```text
starting vertex (n - 1 digits)
+ one appended digit for each of the k^n edges
```

Therefore its length is exactly:

```text
n - 1 + k^n
```

which matches the lower bound.

---

## Step 9: Build the proof from the same model

### Coverage

Every possible length-`n` password corresponds to exactly one graph edge. The DFS/Hierholzer
traversal uses every edge exactly once. Each traversed edge creates its corresponding password as
a length-`n` window. Therefore every password occurs.

### Optimality

There are `k^n` required windows. A string of length `L` has only `L - n + 1` length-`n` windows,
so every solution needs at least `k^n + n - 1` digits. Our construction has exactly that length,
so it is shortest.

### Termination and no duplicates

There are finitely many (`k^n`) edges, and an edge is explored only if it is not in `used`.
Therefore each edge is processed once and recursion terminates.

---

## If I am completely stuck during the interview

I can still make useful progress without recognizing Euler immediately.

### 1. State a brute-force formulation

I can backtrack over digits:

- keep the current suffix of length `n - 1`;
- try appending each digit;
- form the new length-`n` window;
- continue only if that window has not been used;
- succeed after using all `k^n` windows.

This may be exponential if I copy state and backtrack over choices, but it is a correct starting
point. More importantly, it discovers the right state and shows that passwords should be tracked
as used transitions.

### 2. Inspect the structure of that backtracking graph

Every suffix has exactly `k` outgoing and `k` incoming choices. That strong regularity suggests
that I should not need combinatorial trial and error. I need an algorithm that systematically
uses all edges.

### 3. Ask the interviewer a focused question

Instead of saying “I am stuck,” I can say:

> “I have reduced this to traversing every directed edge exactly once in a balanced overlap
> graph. I believe this is an Eulerian traversal; may I proceed with that direction?”

This demonstrates substantial progress and may earn a small hint about Hierholzer if I forgot it.

---

## A realistic interview narration

Here is a concise version of the reasoning I can practice saying:

> “The safe examines every length-`n` sliding window, so the output must contain all `k^n`
> passwords. A length-`L` string has `L - n + 1` such windows, giving a lower bound of
> `k^n + n - 1`. To attain it, every new digit must introduce a new password.
>
> Consecutive passwords overlap in `n - 1` digits, and that suffix is all I need to know to
> choose the next digit. I will make every `(n - 1)`-digit suffix a vertex. Appending a digit
> creates one length-`n` password and moves to the new suffix, so each password is a directed
> edge.
>
> The requirement is now to use every edge once, which is an Eulerian circuit. Every vertex has
> `k` incoming and `k` outgoing edges, and the graph is connected. I can construct the circuit
> with Hierholzer's DFS, marking edges used and recording their final digits in postorder. The
> start suffix plus the reversed edge labels has length `k^n + n - 1`, so it is optimal.”

---

## Common traps and how to redirect myself

### “Shortest” makes me think BFS

Ask: shortest path from what source to what destination? There is no destination here. BFS finds
a shortest route between states; this task requires covering all objects. The counting lower
bound and overlap structure are more informative than the word “shortest.”

### I track visited suffixes

Suffixes must be revisited. For example, multiple passwords can end at the same suffix. The
objects that must not repeat are complete length-`n` passwords, so I track used edges.

### I greedily choose the next digit

A forward greedy path can appear stuck before the whole graph is covered. Use postorder Eulerian
traversal, which builds the valid order as recursion unwinds.

### I search all permutations of passwords

There are `(k^n)!` orderings, which is hopeless. The only relevant relationship between pieces is
their `n - 1` overlap. Compress that overlap into graph vertices.

### I know the term “De Bruijn” but cannot derive the answer

The named pattern is optional. The implementable model is:

```text
(n - 1)-suffix vertices + n-digit password edges + Eulerian circuit
```

That is what I should remember and explain.

---

## Recognition pattern for similar problems

Look for these clues:

- all fixed-length strings/combinations must appear;
- one appended symbol shifts a sliding window;
- consecutive required objects share a fixed suffix/prefix overlap;
- every required piece must be used, preferably once;
- the answer should exploit maximum overlap;
- the current suffix fully determines the next choices.

Then ask:

1. What overlap is sufficient to describe my state?
2. Can overlaps be vertices?
3. Can required pieces be edges?
4. Does the problem become “use every edge exactly once”?
5. Are Eulerian degree and connectivity conditions satisfied?

Related forms include:

- reconstructing a sequence from fixed-length fragments;
- arranging directed pairs so every pair is used once;
- itinerary reconstruction from tickets;
- generating every possible fixed-length pattern once;
- genome assembly from idealized fixed-length `k`-mers.

Not every substring problem is Eulerian. If pieces have different lengths, can be omitted, or do
not share a fixed-size overlap, the problem may instead require dynamic programming, shortest
common superstring techniques, or another model.

---

## Final mental model

Do not memorize only:

```text
LeetCode 753 = De Bruijn sequence
```

Memorize the derivation:

```text
Each typed digit creates one sliding window.
There are k^n windows to cover.
The optimal length is k^n + n - 1.
To attain it, consecutive passwords must maximally overlap.
The last n - 1 digits are the state.
Appending a digit is a password edge.
Every password edge must be used once.
That is an Eulerian circuit.
Hierholzer records edges in postorder.
```

The transferable skill is moving from a sequence problem to an overlap graph. Once the required
pieces become edges, the algorithm becomes much easier to recognize.
