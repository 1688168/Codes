# 489 Robot Room Cleaner
## How is this DFS diff than regular DFS?
* this robot has a direction pointed to. it can only move forward with the direction.  ie. if you direction is pointed to right, we cannot move up.
* due to the direction, we need to record an additional attribute of dir in additional to (x, y) -> (x, y, d)