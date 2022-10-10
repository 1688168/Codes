### Solution 1:  
__Union-find__

Ideas:  
1. Remove duplicates and sort Vals  
2. add (in increasing order) Vals one by one to Union Sets.  
3. after the val added to UnionSets, we count and aggregate how many vals in each disjoint set
4. in each disjoint set, the good path of this new (largest val added) is cnt*(cnt-1)/2*1 (count of combination of 2)

![add0](https://github.com/1688168/Docs/blob/main/objs/2421_0.png "Adding Zero")  
![add1](https://github.com/1688168/Docs/blob/main/objs/2421_1.png "Adding One")  
![add2](https://github.com/1688168/Docs/blob/main/objs/2421_2.png "Adding Two")  
 
### Solution 2:  
__Path in a Tree__
