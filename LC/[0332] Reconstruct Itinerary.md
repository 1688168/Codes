> ## Solution I: DFS
>
> **Why DFS is not a good choice**

- Repeat previous attempts
- Since the problem statements guarantees all tickets will be used, if we reached the destination but didin't use all tickets, this failed attempt will be traverse again (because we have to use all tickets).
- Per above, we are unable to accumulate useful info from failed attempts and avoid repeats
- Back track wastes previous attempts

> ## Eulerian path/trail definition

- In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
- Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex.
- The problem statements guarantees the Euler path exists

> ## Solution II: Eulerian Path

```
         -> D -> E
A -> B  <-> F
        <-> G
```

B + path2 + path1
-> refer to C++ side detailed definition
path1 is deadend
