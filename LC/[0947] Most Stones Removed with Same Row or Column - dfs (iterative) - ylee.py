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
            row_map[xx].append(ii) # row xx has node idx ii
            col_map[yy].append(ii) # rwo yy has node idx ii
        
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
        * try all nodes, and dfs iteratively
        """
        # DFS (iterative) to count connected groups
        # setup stack
        stack = []
        cnt=0
        visited=set()
        
        for idx in range(len(stones)):
            if idx in visited: continue
            stack.append(idx)
            visited.add(idx)
            cnt+=1

            while stack:
        
                # post-order
                curr_node_idx = stack[-1]
                print(" ----- New Group ----- ")

                # dfs all neighbors
                for neighbor_idx in gg[curr_node_idx]: # for each connected node
                    if neighbor_idx not in visited: # if the connected node is NOT visited
                        visited.add(neighbor_idx)   # mark it visited
                        stack.append(neighbor_idx)  # append to stack
                        break # DFS and process the leave node first
                else: # now we are returned to the current node (all leaves nodes were processed)
                    # after finished all processed neighbors
                    if idx != curr_node_idx: # we cannot remove root
                        print(f"All leaves nodes were processed, not remove current stone (node): {curr_node_idx}")
                    stack.pop() # remove this stone go back to previous frame

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