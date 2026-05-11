# <center><b><span style="color:orange">Diff Array, Sweeping Line</span></b></center>

## Pattern
* You will be provided with a list of interval and something is happing during the interval range.  (be careful on interval inclusive/exclusing on ending day)
* the interval can represent timestamps or some index on an x-axis representing location, ... etc.
* after building the events line (ensure sorted by x-axis), we will process each event
  * aggregation for all events
  * for all evets covering this location, who is the max/min (maintain the status until next event point)

## How to represent the events?
* map: 
  * ordered or unordered
* array: 
  * fully represent the largest interval
 
## If you need to maintain order
* To sort the events, we can leverage Java-treeMap to maintain order
* asking Interval Merge: when sum==0 -> we complete interval merge
* asking count of Interval intersect -> each new event, we update max so far



# Sweep Line — Mental Model & Common Use Cases

## Core Mental Model

Sweep line is useful when:

```text
Things become active and inactive over time/space.
```

Instead of thinking about full objects, think about:

```text
events that CHANGE the current state
```

Usually:

- start event → object becomes active
- end event → object becomes inactive

Then:

1. Convert objects into events
2. Sort events
3. Sweep left → right
4. Maintain active state

---

# Master Pattern

```text
Objects affect an interval of time/space.
Their effect starts somewhere and ends somewhere.
```

So:

```text
Represent effect changes as events.
Sort events.
Process changes incrementally.
```

---

# Common Trigger Keywords

## Intervals / ranges

- intervals
- ranges
- segments
- meeting times
- coverage

Mental trigger:

```text
Can I turn each interval into:
(start, +1)
(end, -1)
?
```

---

## Overlap / simultaneous

- overlap
- concurrent
- simultaneous
- ongoing
- active at the same time

Mental trigger:

```text
Track how many are currently active.
```

---

## Timeline processing

- arrivals/departures
- entering/leaving
- opening/closing
- scheduling
- events over time

Mental trigger:

```text
State changes only at event times.
```

---

## Coverage problems

- covered region
- union of intervals
- visible area
- occupied space
- total covered length

Mental trigger:

```text
Coverage only changes at boundaries.
```

---

## “At any moment”

Huge sweep-line trigger.

Examples:
- maximum ongoing meetings
- current users online
- airplanes in the sky

Mental trigger:

```text
Maintain active set while sweeping.
```

---

# Common Sweep Line Problems

## 1. Merge Intervals

Examples:
- LC 56 Merge Intervals
- Employee Free Time

Idea:

```text
Intervals begin/end coverage.
```

---

## 2. Maximum Overlapping Intervals

Examples:
- Meeting Rooms II
- Number of Airplanes in the Sky

Idea:

```text
Track max active intervals.
```

---

## 3. Scheduling / Calendar Problems

Examples:
- booking systems
- room scheduling
- event conflicts

Idea:

```text
Intervals represent occupied time.
```

---

## 4. Skyline Problems

Examples:
- LC Skyline Problem

Idea:

```text
Buildings enter and leave.
Maintain active heights.
```

---

## 5. Geometry Union Problems

Examples:
- Rectangle union area
- Union of segments

Idea:

```text
Coverage changes only at edges.
```

---

## 6. Difference Array Problems

Examples:
- Car Pooling
- Range Addition
- Corporate Flight Bookings

Idea:

```text
Discrete sweep line:
+value at start
-value after end
```

Then reconstruct using prefix sums.

---

# Generic Sweep Line Template

```python
events = []

for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))

events.sort()

active = 0

for x, delta in events:
    active += delta
```

---

# Merge Intervals as Sweep Line

For LC 56:

```text
active > 0
```

means:

```text
currently inside merged interval
```

Merged interval starts when:

```text
active: 0 -> 1
```

Merged interval ends when:

```text
active: 1 -> 0
```

---

# Why Greedy Often Beats Sweep Line

Greedy interval merging is usually preferred because:

- simpler
- less bookkeeping
- fewer edge cases
- same complexity

Both are:

```text
O(n log n)
```

because sorting dominates.

---

# Key Insight

Sweep line works when:

```text
The state only changes at critical points.
```

So instead of processing every point:

```text
Process only the moments where something changes.
```