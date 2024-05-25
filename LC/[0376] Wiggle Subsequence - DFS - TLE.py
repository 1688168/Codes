class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        # I/O: 
        + nums
        => longest wiggle subsequence of nums

        # Analysis:
        + N=1000
        [Bruteforce:]
        > DFS:
        * 2^1000

        [DP:] 

        # Q:
        * why is this not type II?
        * VS LIS
        """
        N=len(nums)
        mxl=0
        def dfs(st, prev, expected_flag, curr_len):
            nonlocal mxl
            mxl=max(mxl, curr_len)

            if st >=N: return
        
            if prev is None: #pick the first element
                dfs(st+1, st, None, curr_len+1)
                dfs(st+1, None, None, curr_len)
                return
            
            if expected_flag is None: # pick the 2nd element
                if nums[st] != nums[prev]:
                    dfs(st+1, st, (nums[st]-nums[prev])< 0, curr_len+1)
                dfs(st+1, prev, expected_flag, curr_len)
                return
            
            if expected_flag: #looking for postive
                if nums[st] > nums[prev]:
                    dfs(st+1, st, not expected_flag, curr_len+1)
                dfs(st+1, prev, expected_flag, curr_len)
              
                return
            else: # looking for negative
              if nums[st] < nums[prev]:
                    dfs(st+1, st, not expected_flag, curr_len+1)
              dfs(st+1, prev, expected_flag, curr_len)
              return
            
        dfs(0, None, None, 0)
        return mxl       