### Solution 1:  Union-find
`Summary:`
1. add val one-by-one in increasing order into Disjoint Set.  
2. for each root of the disjoint set, count the number of val
3. cnt of good path is n(n-1)/2*1


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
 
 
 
### Solution 2:  Path in a Tree
`Summary:`
1. For each node in the Tree (converted to graph), how many good path connected to this node?
2. Starting index=0, DFS all children and calc good path.

`Ideas:`
1. convert the tree to graph as we need to traverse all connected path
2. when traversing the branch, skip when child == parent (similar to visited)
3. use the smaller branch to look up from big branch (look up is expensive)

`Implementation steps:`
1. convert the tree to graph
2. dfs starting from index=0
3. for all children, remove all nodes with value < curr (not qualified for good path)

