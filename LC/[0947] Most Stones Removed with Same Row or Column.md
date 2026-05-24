# 947
## Problem Statement
* max num of stones we can remove

## rules
* we can remove all stones (except 1) in any column or row

## Thoughts
* given a group, we only need to keep one stone
-> this is a grouping question
-> DSU(Union/Find)

## Mental model
* Consider each row and each col is a node
* each time we place a stone we connect (union/group) the row and col
* processing each stone, we will identify num of groups (connected row and col)
* numOfStone-numOfGroups = numOfMaxStonesCanBeRemoved

## complexity analysis
* Union/Find (path compression+UninoBySize) -> N(Alpha(N^2))
* N=10^4 -> alpha(10^8) -> okay