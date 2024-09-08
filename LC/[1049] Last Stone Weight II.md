> why this is a KNAPSACK problem.

For any sequence of operations, the algebra boils down to difference of two sums

For example,
(((a - b) - c) - d) = a - b - c - d = (a) - (b + c + d)
((d - (a - b) )- c) = d - a + b - c = (d + b) - (a + c)

Given that if there are two or more items, we have to do a subtraction ( two stones reduce to 0 or another stone ), it's guaranteed that there will be two groups of items.  

This is why, the original problem of finding the smallest difference (remaining stone) reduces to <span style="color:red">**finding two complementary sets of (mutually exclusive) items**</span>, with the idea that:  

the potential answer to the question is the difference of the sums of these two groups
this is an optimization problem, so we want to minimize the difference between the sums
The optimization problem explained:

* Since we are finding two complementary sets of items, it's sufficient to find one set. (The other one is complementary!)  
  
* We are interested in minimizing the difference in sums of these sets.  
* The sets are not empty. In other words we can't have all items in one set.  
* <span style="color:red">So this reduces to the problem of finding a set whose sum is as close to total / 2 as possible.</span>   
* Because the sum of the complementary set will be total - this_sum. Hence the "potential" answer will be <span style="color:orange">(total - this_sum) - this_sum</span>

-- This value to be minimum we want total - 2 * this_sum ==> 0 (close to 0)  
--- This means total ==> 2 * this_sum  
--- Meaning this_sum ==> total / 2  

<span style="color:red">**This is a knapsack problem where we want to find a set of items that sum to a maximum of total / 2, maximally**</span> so. We are only limited by the sum having to be <= total / 2.  

> So how do we solve this problem?   
* Find all subsets of the original set, 
* find their sum, keep track of the sum that is <= total / 2. 

* If we ever reach sum = total / 2, we are done. No need to keep going. 

* If we reach sum > total / 2 discard those values.

> This author's solution for generating all possible combinations is:

-- keep track of sums with each item included or not included, in combination with already generated sets. (I know this is kind of oversimplified, that's what it is)  

> Here is a slightly more readable, slightly optimized version of the original code submitted by this author:  

> YLee Notes:  

[`classic Knapsack problem`]  
* Given a list of resource with attributes (profit, cost) and capacity.  max profit under capacity

[`Variation`]
* partition the resource to two groups and minimize the diff
* total=sum(A)+sum(B)
* so the problem reduced to find a subset A that sum upto total/2. (remember whatever not in A is in the complement set B)
* each item is take/skip to A
* of sum(A)==total/2 --> return 0 (anything not pick is in B)
* we can just keep track min(sum(A))

```python
class Solution:
    def lastStoneWeightII(self, stones):
        sums_of_groups = {0} # keep track candidates
        total = sum(stones)  # get total weight
        
        for weight in stones: #for each stone
            addition_sums_of_groups = set() #starting from empty for each stone
            for sum_of_group in sums_of_groups: #existing candidates
                if weight + sum_of_group <= total // 2:                    
                    addition_sums_of_groups.add(weight + sum_of_group)
                elif weight + sum_of_group == total // 2: #sum(A)=total/2 --> the rest is automatically in B
                    return 0
            sums_of_groups |= addition_sums_of_groups #merging existing candidate with new candidates
                    
        return min(abs(total - sum_of_group - sum_of_group) for sum_of_group in sums_of_groups)
        
```