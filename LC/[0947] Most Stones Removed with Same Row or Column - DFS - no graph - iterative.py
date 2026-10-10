class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        N=len(stones)
        visited=set()
        stack=[]
        cnt=0

        def is_connected(aa, bb):
            return (stones[aa][0] == stones[bb][0]) or (stones[aa][1] == stones[bb][1])

        for ii in range(N):
            if ii in visited: continue
            visited.add(ii)
            stack.append([ii, 0])
            cnt += 1
            while stack:
                curr_idx, neighbor_idx = stack[-1]
                stack[-1][-1] += 1

                if neighbor_idx == N: # we have visited all neighbors
                    stack.pop()
                    continue

                if neighbor_idx==curr_idx: continue
                if neighbor_idx in visited: continue
                if not is_connected(curr_idx, neighbor_idx): continue
                visited.add(neighbor_idx)
                stack.append([neighbor_idx, 0])

        return N-cnt