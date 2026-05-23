# OpenAI SDE Interview: 25-Problem LeetCode Study Plan

OpenAI's engineering interviews heavily index on practical system implementation, string parsing (highly relevant for LLM inputs/outputs), deep graph/tree traversals, and advanced data structure design. This 25-problem plan is optimized for the patterns most frequently seen in their SDE loops.

## Week 1: String Manipulation & Parsing
OpenAI deals heavily with text streams, tokenization, and AST (Abstract Syntax Tree) parsing. Mastery of string manipulation and stack-based parsing is non-negotiable.

- [ ] **1. Valid Parentheses** (Easy - #20) - *Warm-up for stack logic.*
- [ ] **2. Basic Calculator II** (Medium - #227) - *Crucial for parsing and evaluating expressions.*
- [ ] **3. Decode String** (Medium - #394) - *Nested parsing using stacks.*
- [ ] **4. Text Justification** (Hard - #68) - *Tests your ability to handle tedious edge cases and array/string formatting.*
- [ ] **5. Regular Expression Matching** (Hard - #10) - *Advanced string matching and dynamic programming.*

## Week 2: Trees & Graph Traversal
Representing neural networks, routing requests, and managing dependencies all require strong graph and tree fundamentals.

- [ ] **6. Number of Islands** (Medium - #200) - *Fundamental grid traversal (DFS/BFS).*
- [ ] **7. Clone Graph** (Medium - #133) - *Tests deep copying of pointer-based structures.*
- [ ] **8. Course Schedule** (Medium - #207) - *Topological sorting and cycle detection (dependency resolution).*
- [ ] **9. Lowest Common Ancestor of a Binary Tree** (Medium - #236) - *Fundamental recursion.*
- [ ] **10. Binary Tree Maximum Path Sum** (Hard - #124) - *Advanced tree traversal and state tracking.*
- [ ] **11. Serialize and Deserialize Binary Tree** (Hard - #297) - *Highly relevant for transmitting structural data over a network.*

## Week 3: Data Structure Design
System design interviews at AI companies often bleed into the coding rounds. You need to know how to build custom, optimized data structures from scratch.

- [ ] **12. Implement Trie (Prefix Tree)** (Medium - #208) - *Essential for text search, autocomplete, and token routing.*
- [ ] **13. Design Add and Search Words Data Structure** (Medium - #211) - *Trie combined with DFS backtracking.*
- [ ] **14. LRU Cache** (Medium - #146) - *A classic. Tests hash maps and doubly linked list integration.*
- [ ] **15. LFU Cache** (Hard - #460) - *A step up from LRU; great for showing mastery of time complexity optimization.*
- [ ] **16. Design In-Memory File System** (Hard - #588) - *Object-oriented design mixed with Trie/N-ary tree logic.*
- [ ] **17. All O`one Data Structure** (Hard - #432) - *Constant time $O(1)$ operations for tracking maximum and minimum string frequencies.*

## Week 4: Optimization, Arrays & DP
These problems test your ability to optimize mathematical operations, manage memory footprints, and solve state-based problems efficiently.

- [ ] **18. Product of Array Except Self** (Medium - #238) - *Prefix/Suffix arrays without division.*
- [ ] **19. Merge Intervals** (Medium - #56) - *Sorting and boundary logic.*
- [ ] **20. Next Permutation** (Medium - #31) - *Array manipulation and in-place algorithms.*
- [ ] **21. Trapping Rain Water** (Hard - #42) - *Two-pointer optimization technique.*
- [ ] **22. Evaluate Division** (Medium - #399) - *Graph logic applied to math/equations.*
- [ ] **23. Edit Distance** (Medium - #72) - *Classic DP, highly relevant to spell-checking and NLP/tokenization concepts.*

## Week 5: Advanced & Distributed Systems Concepts
High-signal problems that test your ability to handle search spaces and complex pathfinding algorithms often used in routing and ML infrastructure.

- [ ] **24. Swim in Rising Water** (Hard - #778) - *Dijkstra's Algorithm / Priority Queues.*
- [ ] **25. Word Ladder** (Hard - #127) - *Shortest path in an unweighted graph (BFS).*