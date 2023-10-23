> Solution I

1. build graph
2. build matrix that records distance btn any two nodes.
   - per DFS. for each node, for each child
3. for each query
   - use matrix to check distance
   - find next node on the path and inspect if the distance is shorter
   - for formula to check if child is on the path
   - matrix[curr][end]==matrix[j][end]+1 [`Genius`]

> Solution II

1. build graph
2. dfs find the path
3. bfs from node to path
