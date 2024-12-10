> Problem Statement:
* guess a num from 1~N, if you guess x and wrong, you pay x.
* if you guess right, you pay nothing
* you win if you got it right before use up all your money
-> The min money you need to have to guarantee a win given n


> Analysis:
1 2 3 4 5 6 7 8 9 
        x
        
* bruteforce
* greedy




> How can you identify this as DP Type IV?
1. you are given an N which represents an interval [1, n]
2. each time you pick x, you partition the interval into [1, x-1], [x+1, n]
3. we are trying to find the optimal solution (min money) you need to win interval [1, n]
4. can optinal solution for interval [1, n] be derived from sub-intervals?
