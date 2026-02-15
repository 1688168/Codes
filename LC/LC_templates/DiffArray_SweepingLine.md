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
