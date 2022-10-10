### Solution 1:  
__Union-find__

`Ideas:`
1. Remove duplicates and sort Vals  
2. add (in increasing order) Vals one by one to Union Sets.  
3. after the val added to UnionSets, we count and aggregate how many vals in each disjoint set
4. in each disjoint set, the good path of this new (largest val added) is cnt*(cnt-1)/2*1 (count of combination of 2)

![add0](https://github.com/1688168/Docs/blob/main/objs/2421_0.png "Adding Zero")  
![add1](https://github.com/1688168/Docs/blob/main/objs/2421_1.png "Adding One")  
![add2](https://github.com/1688168/Docs/blob/main/objs/2421_2.png "Adding Two")  
 
 5. ttl cnt = accumulated cnt + ttl_node_cnt (individual node is a valid good path)
 
`Implementation steps:`
 1. build union/find data structure (with rank optimization)  
 2. build graph of the tree (vertex=value, children: (a, b) where a is the index of the vertex, b is the index with smaller value where a is connected to)  
 3. sort and remove duplicate of vals.  
 4. build val2idx map: given an val, what are the index of this val  
 5. adding unique/sorted vals one by one to the union  
  5.1 add val to union/set  
  5.2 for all index of this val, count the val for each root of the disjoint set  
  5.3 aggregate the cnt  
 6. ttl cnt = aggregated_cnt + len(vals)  
 
 
 
### Solution 2:  
__Path in a Tree__
