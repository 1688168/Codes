class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        * N=5*10^4 -> 5*10^4*(2*10) -> 10^6
        """
        N = len(arr)
        # preprocess val2idx
        val2idx=defaultdict(list)
        for ii, nn in enumerate(arr):
            val2idx[nn].append(ii)
        
        # prepare BFS (shortest distance/min jump requred to reach end)
        qq = deque()
        level=0
        visited=set() 

        # initialize root node
        qq.append(0)
        visited.add(0)

        while (sz:=len(qq)) > 0:
            if N-1 in visited: return level
            for _ in range(sz): #for the level   
                curr_idx = qq.popleft()
                curr_val = arr[curr_idx]
                prev_idx = curr_idx-1
                next_idx = curr_idx+1

                # consider prev
                if prev_idx >=0 and prev_idx not in visited:
                    visited.add(prev_idx)
                    qq.append(prev_idx)
                
                # consider next
                if next_idx < N and next_idx not in visited:
                    visited.add(next_idx)
                    qq.append(next_idx)
                
                # consider idx with same values
                if curr_val in val2idx:
                    for idx in val2idx[curr_val]:
                        if idx in visited: continue
                        visited.add(idx)
                        qq.append(idx)
                    
                    del val2idx[curr_val]

            level+=1

        return -1 # if not reaching end