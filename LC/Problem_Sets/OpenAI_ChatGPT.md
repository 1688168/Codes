# OpenAI SDE Interview — 25 LeetCode Study Plan

# Goal

This plan optimizes for:
- strong algorithmic fundamentals
- practical coding interview performance
- high-signal patterns OpenAI-style interviews often value:
  - graph reasoning
  - clean implementation
  - systems thinking
  - interval/event reasoning
  - DSU
  - BFS/DFS
  - heaps
  - shortest paths
  - dynamic programming
  - parsing/simulation

This is NOT:
```text
“memorize 300 LeetCode problems”
```

Instead:

```text
master a small set of high-value patterns deeply
```

---

# Suggested Schedule

| Phase | Focus | Questions |
|---|---|---|
| 1 | Core coding fluency | 1–8 |
| 2 | Graphs + traversal | 9–15 |
| 3 | Advanced patterns | 16–21 |
| 4 | Hard interview-level reasoning | 22–25 |

---

# PHASE 1 — Core Coding Fluency

These should become effortless.

---

## 1. Two Sum
Difficulty: Easy

### Learn
- Hash map lookup
- Complement pattern

### Must Master
```python
seen[target - x]
```

---

## 2. Valid Parentheses
Difficulty: Easy

### Learn
- Stack simulation
- Parser intuition

Important for:
- interpreters
- token parsing
- structured reasoning

---

## 3. Merge Intervals
Difficulty: Medium

### Learn
- Interval sorting
- Active interval mental model

---

## 4. Binary Search
Difficulty: Easy

### Learn
- Search boundaries
- Monotonic conditions

Absolutely mandatory.

---

## 5. K Closest Points to Origin
Difficulty: Medium

### Learn
- Heap basics
- Top-K pattern

---

## 6. Top K Frequent Elements
Difficulty: Medium

### Learn
- Heap + hashmap
- Frequency counting

---

## 7. LRU Cache
Difficulty: Medium

### Learn
- HashMap + doubly linked list
- O(1) system design thinking

Very important.

---

## 8. Number of Islands
Difficulty: Medium

### Learn
- DFS/BFS traversal
- Connected components

Foundational graph problem.

---

# PHASE 2 — Graphs and Traversal

OpenAI-style interviews strongly favor graph intuition.

---

## 9. Clone Graph
Difficulty: Medium

### Learn
- Graph copying
- DFS/BFS with memoization

---

## 10. Course Schedule
Difficulty: Medium

### Learn
- Topological sort
- Cycle detection

Core DAG reasoning.

---

## 11. Pacific Atlantic Water Flow
Difficulty: Medium

### Learn
- Reverse BFS/DFS thinking
- Multi-source traversal

Excellent mental flexibility builder.

---

## 12. Word Ladder
Difficulty: Hard-

### Learn
- BFS shortest path
- Implicit graphs

One of the most important BFS problems.

---

## 13. Network Delay Time
Difficulty: Medium+

### Learn
- Dijkstra
- Priority queue shortest paths

---

## 14. Redundant Connection
Difficulty: Medium

### Learn
- Union Find
- Cycle detection

DSU foundation.

---

## 15. Number of Islands II
Difficulty: Hard-

### Learn
- Dynamic connectivity
- Online Union Find

Very high-value interview problem.

---

# PHASE 3 — Advanced Patterns

Now combine structures and reasoning.

---

## 16. Minimum Interval to Include Each Query
Difficulty: Hard-

### Learn
- Offline sorting
- Sweep line + heap

Very strong interview signal.

---

## 17. Task Scheduler
Difficulty: Medium

### Learn
- Greedy scheduling
- Frequency reasoning

---

## 18. Design Twitter
Difficulty: Medium

### Learn
- Heap merge
- Object-oriented design

Very realistic interview problem.

---

## 19. Accounts Merge
Difficulty: Medium+

### Learn
- DSU grouping
- Hashing + graph connectivity

---

## 20. Trapping Rain Water
Difficulty: Hard-

### Learn
- Two-pointer invariant reasoning

Extremely important interview intuition.

---

## 21. Serialize and Deserialize Binary Tree
Difficulty: Hard-

### Learn
- Tree encoding
- Recursive structure design

Excellent signal problem.

---

# PHASE 4 — Harder OpenAI-Level Reasoning

These test deeper abstraction ability.

---

## 22. Alien Dictionary
Difficulty: Hard-

### Learn
- Graph construction from constraints
- Topological ordering

Very “LLM/parser/reasoning” flavored.

---

## 23. Basic Calculator II
Difficulty: Medium+

### Learn
- Parsing
- Expression evaluation
- State machines

Extremely useful.

---

## 24. Sliding Window Maximum
Difficulty: Hard-

### Learn
- Monotonic deque
- Streaming optimization

Important systems/data-stream pattern.

---

## 25. Minimum Cost to Connect All Points
Difficulty: Hard-

### Learn
- MST
- Kruskal/Prim
- Graph optimization

Excellent final graph problem.

---

# Most Important Patterns to Master

| Pattern | Problems |
|---|---|
| HashMap | 1, 6 |
| Stack/parser | 2, 23 |
| Intervals | 3, 16 |
| Binary search | 4 |
| Heap | 5, 6, 13, 16, 18 |
| DFS/BFS | 8–12 |
| Topological sort | 10, 22 |
| Union Find | 14, 15, 19 |
| Greedy | 17 |
| Trees | 21 |
| Sliding window/deque | 24 |
| MST | 25 |

---

# OpenAI Interview Mental Model

OpenAI interviews often reward:

## 1. Clear thinking
Not:
```text
memorized tricks
```

But:
```text
clean decomposition
```

---

## 2. Strong implementation quality

Expectations:
- bug-free code
- edge cases
- readable naming
- communication

---

## 3. Graph reasoning

Very important:
- BFS
- DAGs
- shortest paths
- connectivity

---

## 4. Systems-style thinking

Especially:
- heaps
- streaming
- scheduling
- caching
- parsing

---

# Recommended Practice Strategy

For EACH problem:

## Pass 1
Solve normally.

---

## Pass 2
Write:
- time complexity
- space complexity
- core invariant
- mental trigger

---

## Pass 3
Re-solve from scratch 2–3 days later.

---

# What You Should Eventually Recognize Instantly

| Trigger | Pattern |
|---|---|
| “shortest path” | BFS/Dijkstra |
| “dependency ordering” | topo sort |
| “merging groups” | DSU |
| “active intervals” | heap/sweep |
| “streaming max/min” | monotonic deque |
| “many overlapping intervals” | sweep line |
| “design O(1)” | hashmap + linked list |
| “evaluate expression” | stack/parser |

---

# Final Advice

OpenAI-style interviews are less about:
```text
memorizing obscure tricks
```

and more about:
```text
clean abstraction + implementation quality
```

A candidate who deeply understands:
- BFS
- heaps
- DSU
- interval reasoning
- parsing
- graph construction

will usually outperform someone who memorized 500 random problems.