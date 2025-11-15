# <center><b><span style="color:orange">Diff Array, Sweeping Line</span></b></center>

> # <b><span style="color:purple">Pattern</span></b>
* it will be something relating to interval and each interval has some numbers. count, or height of building. 
* you will be givne list of (start, end).  We will model those timestamps into (start, 1), (end, -1) as events
* the interval can represent timestamps or some strightline index
* after building the events line we can leverage on it and find out
  * max overlap
  * find intervals that is not covered by any given intervals
  * avg of merged intervals (interval count with interval value)

> # <b><span style="color:purple">How to represent the events?</span></b>
* map: 
  * ordered or unordered
* array: 
  * fully represent the largest interval
 
> # <b><span style="color:purple">If you need to maintain order</span></b>
* To sort the events, we can leverage Java-treeMap to maintain order
* asking Interval Merge: when sum==0 -> we complete interval merge
* asking count of Interval intersect -> each new event, we update max so far
