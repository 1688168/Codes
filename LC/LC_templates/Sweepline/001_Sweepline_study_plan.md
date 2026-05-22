# Sweep Line Study Plan (LeetCode)

# Core Mental Model

Sweep line means:

```text
Process events in sorted order while maintaining some active state.
```

Usually:

```text
Sort by x/time/position
→ sweep from left to right
→ maintain currently active intervals/items
```

The key insight:

```text
Instead of thinking globally,
process changes only when events happen.
```

---

# What Is an "Event"?

Typical events:

| Problem Type | Event |
|---|---|
| Intervals | start/end |
| Geometry | entering/leaving |
| Calendar | meeting starts/ends |
| Skyline | building begins/ends |
| Range coverage | add/remove interval |
| Active sets | insertion/deletion |

---

# The 4 Core Sweep Line Patterns

| Pattern | Main Data Structure |
|---|---|
| Counting overlaps | counter |
| Active intervals | heap |
| Ordered active elements | TreeMap / SortedList |
| Coordinate compression + diff array | prefix sums |

---

# Study Order

The progression:

```text
Intervals
→ overlap counting
→ active heap
→ event sorting tricks
→ ordered active structures
→ geometry
→ advanced active-set reasoning
```

---

# PHASE 1 — Basic Event Counting

## 1. 252. Meeting Rooms
Difficulty: Easy

### Learn
- Interval overlap intuition
- Sorting by start time

### Mental Model
```text
Can meetings coexist?
```

This introduces interval reasoning before true sweep line.

---

## 2. 253. Meeting Rooms II
Difficulty: Medium

### Learn
- True sweep line
- Start/end events
- Active interval count

### Key Insight

Convert:

```text
[start, end]
```

into:

```python
(start, +1)
(end, -1)
```

Sweep through events:

```text
running count = active meetings
```

Maximum active count = answer.

---

# PHASE 2 — Difference Array Sweep

## 3. 1094. Car Pooling
Difficulty: Medium

### Learn
- Difference array sweep line
- Capacity tracking

### Mental Model

Passengers enter/leave:

```python
(start, +numPassengers)
(end, -numPassengers)
```

Very important pattern.

---

## 4. 1109. Corporate Flight Bookings
Difficulty: Medium

### Learn
- Range increment optimization
- Prefix sum sweep

### Key Insight

Instead of updating every index in range:

```python
diff[l] += val
diff[r+1] -= val
```

Then prefix sum reconstructs active effect.

This is sweep line on arrays.

---

# PHASE 3 — Active Interval Structures

## 5. 56. Merge Intervals
Difficulty: Medium

### Learn
- Interval merging
- Maintaining active interval

### Mental Model

```text
Current interval stays active
until a non-overlapping interval appears.
```

One of the most important interval problems.

---

## 6. 57. Insert Interval
Difficulty: Medium

### Learn
- Sweep-like interval transitions
- Overlap state changes

### Important
Build intuition for:
- before overlap
- during overlap
- after overlap

---

# PHASE 4 — Heap-Based Sweep Line

## 7. 1851. Minimum Interval to Include Each Query
Difficulty: Hard-

### Learn
- Offline sorting
- Heap of active intervals

### Major Mental Model

```text
As queries move right,
activate intervals that now cover the query.
```

Heap stores:
- active intervals
- prioritized by smallest size

This is one of the most important sweep-line patterns.

---

# PHASE 5 — Geometry Sweep Line

## 8. 218. The Skyline Problem
Difficulty: Hard

### Learn
- Entering/leaving building events
- Max heap active heights
- Critical points

### Core Insight

Buildings generate:

```text
start event
end event
```

Sweep line maintains:
```text
current tallest active building
```

This is THE classic sweep-line problem.

---

# PHASE 6 — Ordered Active Sets

## 9. 759. Employee Free Time
Difficulty: Hard-

### Learn
- Multi-list interval sweep
- Shared active intervals

### Mental Model

```text
Find gaps between active working intervals.
```

Very strong interval intuition builder.

---

# PHASE 7 — Advanced Sweep + Ordered Structures

## 10. 850. Rectangle Area II
Difficulty: Hard

### Learn
- 2D sweep line
- Nested sweep logic
- Coordinate compression
- Segment tree intuition

### Why Final

This is advanced sweep-line mastery.

You learn:
- vertical sweep
- maintaining covered y-intervals
- area accumulation

Very important for competitive programming.

---

# Recommended Study Order

| Stage | Problem | Main Idea |
|---|---|---|
| 1 | 252 | Interval overlap |
| 2 | 253 | Event counting |
| 3 | 1094 | Difference array sweep |
| 4 | 1109 | Prefix sum sweep |
| 5 | 56 | Interval merging |
| 6 | 57 | Overlap transitions |
| 7 | 1851 | Heap active intervals |
| 8 | 218 | Skyline sweep |
| 9 | 759 | Multi-interval sweep |
| 10 | 850 | 2D geometry sweep |

---

# Master Mental Models

By the end, you should instantly recognize:

| Pattern | Recognition Trigger |
|---|---|
| Event counting | starts/ends |
| Active intervals | overlapping ranges |
| Heap sweep | smallest/largest active |
| Difference array | many range updates |
| Offline sweep | sort queries + intervals |
| Geometry sweep | entering/leaving shapes |
| Ordered active set | nearest/current active |
| Coordinate compression | huge coordinates |

---

# Universal Sweep Line Thought Process

When reading a problem:

## Step 1
Ask:

```text
Can I process changes in sorted order?
```

Usually:
- time
- x-coordinate
- positions
- interval endpoints

---

## Step 2
Ask:

```text
What are the events?
```

Examples:
- interval starts
- interval ends
- building enters/leaves
- passenger enters/leaves

---

## Step 3
Ask:

```text
What must stay active during the sweep?
```

Examples:
- active intervals
- active heights
- active meetings
- active coverage

---

## Step 4
Choose active structure

| Need | Structure |
|---|---|
| count | integer |
| min/max active | heap |
| ordered active | TreeMap/SortedList |
| range coverage | segment tree |

---

# Most Important Insight

Sweep line is fundamentally:

```text
Turn global overlap problems
into local event transitions.
```

That is the deep mental model.

---

# Complexity Intuition

Most sweep-line problems become:

```text
Sort events: O(N log N)
Process events: O(N log N)
```

because:
- sorting dominates
- heap/tree operations are log N

---

# After These 10

## More Advanced Sweep Line

- 391. Perfect Rectangle
- 732. My Calendar III
- 352. Data Stream as Disjoint Intervals
- 699. Falling Squares
- 2406. Divide Intervals Into Minimum Number of Groups

## Advanced Geometry

- Line segment intersection
- Closest pair of points
- Bentley–Ottmann algorithm

These become much easier after mastering sweep line.