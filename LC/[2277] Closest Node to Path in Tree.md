> Solution I: build distance matrix and

1. build graph/tree
2. build matrix that records distance btn any two nodes.
   - per DFS. for each node, for each child
   - or BFS (should be same performancewise we tree has no circle, only one path btn any two nodes)
3. for each query
   - use matrix to check distance
     a. default (node, path) distance as math.inf
     b. from (node, start) and keep track min distance
     c. find next node on path per: distance(curr, end) = 1+distance(curr_child, end)
     d. once we find next child, see if (node, child) distance is shorter and update ans
     e. exit state: if curr==end
   - find next node on the path and inspect if the distance is shorter
   - for formula to check if child is on the path
   - matrix[curr][end]==matrix[j][end]+1 [`Genius`]

> Solution II

1. build graph
2. dfs find the path
3. bfs from node to path
