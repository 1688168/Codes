# 947

# Problem Statement
## Given
* list of stone coordinates (2D plane)
* rules to remove stones

## ask
* max num of stones can be removed per the given rule

# Constraints analysis
* N=1~1K
* plane size = 10^4
## edge cases consideration (partial credit)
* if N=1 -> return 0

## Mental model (union-find)
* Consider each row and each col is a node
* each time we place a stone we connect (union/group) the row and col
* processing each stone, we will identify num of groups (connected row and col)
* numOfStone-numOfGroups = numOfMaxStonesCanBeRemoved

## Mental Model (DFS)
* nodes sharing row or columns meaning they are connected in a graph
* if we build the graph representation of the inputs. and post order removing leaves we will be able to know the orders of how to remove leaves and keep only the root

> but how do you know where to start as the root?
* this actually doesn't matter, we can start from any node. Try the below simple example. We can start from any node in the graph and apply post-order DFS.  The root node (doesn't matter which one you pick) will be the last node being processed and should NOT be removed
          *
          |
          *
        /.  \
       *.    *


## complexity analysis
* Union/Find (path compression+UninoBySize) -> N(Alpha(N^2))
* N=10^4 -> alpha(10^8) -> okay


# What did we learn from this problem and the take away
## How is this relating to DFS?
* for grouping, we think of UnionFind, but DFS can also mark all connected cells (Num of Islands)
* from observation, we should notice for connected nodes, eventually one node (stone) will survive if we prune the leave nodes in the right order.  With this observation, we know num of remaining nodes is num of the independent groups.  Num of nodes we can remove is totalNumOfNodes-NumOfConnectedGroups

## Concepts we practiced
* How to do Union-Find in 2D grid. How to encode 2D grid cell coordinates 
* What's the application of DFS -> count connected cells (num of Island variation)
* How to prune leaf-nodes first? or how to record prune sequence -> post-order traversal
* How to do DFS iteratively, recursively
* How to build graph representation of connected nodes in O(N) time and avoid O(N^2) time to build the full representation of the graph

# follow up questions
| LeetCode # | Problem | Similar idea |
|---:|---|---|
| 366 | Find Leaves of Binary Tree | Remove leaves / postorder |
| 310 | Minimum Height Trees | Peel graph from outside inward |
| 210 | Course Schedule II | Construct valid order |
| 1110 | Delete Nodes And Return Forest | Postorder deletion |
| 582 | Kill Process | Dependency/tree traversal |
| 269 | Alien Dictionary | Build graph order from constraints |
| 207 | Course Schedule | Detect dependency feasibility |