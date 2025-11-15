### Situation

##### Given
* straight street
* buildings = [[1,5,2],[3,10,4]] ->  [[starti, endi, heighti]] -> half closed

##### Ask
* min num of non-overlapping segments
* street[j] = [leftj, rightj, avgj] -> in this segment, all buildings together have same avg height
* avg is zero if no building
* 
### Analysis
* N: 10^5 -> nlogn

##### Bruteforce
* for each buildings[ii] - N
  * populate height: *N
** N^2
* calc avg +N
* output segment +N

##### Thinking NLogN
* we are given intervals - sweepline, DP

##### Sweepline
* convert to events - N
* count: number of buildings @ii: +N
* heights: total heights of all buildings @ii: +N
* calc avg height @ each ii: +N
* output segment: +N
-> 4N


### implementation strategy

