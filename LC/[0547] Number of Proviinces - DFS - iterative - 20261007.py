class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N=len(isConnected) #size of cities
        
        stack=[] # for iterative dfs
        visited=set()

        cnt=0 # count group of connected cities

        for ii in range(N): # we need to dfs all cities
            if ii in visited: continue #if the city already part of prior identified groups, we skip
            cnt+=1
            visited.add(ii)
            stack.append([ii, 0])

            while stack: # DFS - iteratively
                curr, idx=stack[-1]

                stack[-1][1] += 1 #increment for next candidate
                if idx >= N: # we finished traversal
                    stack.pop()
                else:
                    # we need to dfs all connected nodes
                    if isConnected[curr][idx] and idx not in visited:
                        visited.add(idx)
                        stack.append([idx, 0])
        return cnt