class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        N=len(stones)

        # Build the graph
        """
        * we are practicing DFS
        * we just need to build the graph that ensure connected nodes are connected via edge, we do NOT need to capture all edges as long as nodes are connected
        """
        row_map = defaultdict(list)
        col_map = defaultdict(list) 

        ## build the col/row map
        for ii, (xx, yy) in enumerate(stones):
            row_map[yy].append(ii) # row YY has node idx ii
            col_map[xx].append(ii) # rwo xx has node idx ii
        
        ## build the graph for connected ndoes
        gg=defaultdict(set)
        for connected in row_map.values():
            first = connected[0]
            for other in connected[1:]:
                gg[first].add(other)
                gg[other].add(first)

        for connected in col_map.values():
            first = connected[0]
            for other in connected[1:]:
                gg[first].add(other)
                gg[other].add(first)

        """
        > now we have the graph
        * we first do recursive (post-order) traversal
        * try all nodes, and DFS to mark visited
        """
        # DFS (recursive) to count connected groups
        def dfs(idx, isStart):
            # we will do post-order traversal
            for connected_idx in gg[idx]:
                (xx, yy) = stones[connected_idx]
                if connected_idx in visited: continue
                visited.add(connected_idx)
                dfs(connected_idx, False)

            if not isStart:
                #print(f"prune node: ", idx)    
                pass
        
        cnt=0
        visited=set()

        for idx in range(len(stones)):
            (xx, yy) = stones[idx]
            if idx in visited: continue
            cnt+=1
            visited.add(idx)
            # print(" ----- new group ----")
            dfs(idx, True)

        # output ttlStonesNum - NumOfGroups
        return len(stones) - cnt


# # Problem Statement
# * Given coordinates of stones on a 2D plane
# * Given rule to remove a stone (connected via same row/col)
# * -> max stone you can remove

# # Observations
# * connected stones can conser as a group
# * each connected group will have one stone left
# * grouping: UnionFind (all stone in same group have same parent) -> total stones - numOfParent = maxStonesWeCanRemove
# * Similar to count Island DFS problem (connected rule is diff). if we use DFS count num of group, this is equivalent to numOfParents via UnionFind

# # Constrain Analysis
# * N=1000 -> We can do N^2
# * N=1 -> return 0 -> partial credit

# # Complexity Analysis
# * DFS=N^2 or N
# * unionFind=AlphaN