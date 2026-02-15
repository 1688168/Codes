# 2158 Amount of New Area Painted Each Day

## Problem Statements
* given paint[ii] = [start, end) --- range/interval (sweepline/diff array)
  where ii is the iith day, you can paint unpainted area between [start, end) non-inclusive
* worklog[ii] = amount of new area that you painted on the iith day (skip areas painted in prior days)

## Analysis
* N=10^5 --- nlogn

> `Bruteforce`
* for each range: N
  * check net increment (r5*10^4) ---> 5*10^9

> `Diff Array` ----> can we only process those turning points?
for each turning points (start, end) points ---> events ---> 2*N
    * who is the effective paint at location ii? (the first paint sorted by date dd at location ii)