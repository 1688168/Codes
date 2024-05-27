class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxl=0
        N=len(nums)
        def dfs(st, flipped, curr_len):
            nonlocal mxl
            if st >= N:
                return

            if nums[st]==0: # got an zero
                if flipped: # already flipped
                    dfs(st+1, False, 0) # ignore current and move on
                    mxl=max(mxl, 1)
                    dfs(st+1, True, 1) # assume this is flipped as beginning
                   
                else: # not flipped yet
                    flipped=True # flip this one
                    mxl=max(mxl, curr_len+1)
                    dfs(st+1, flipped, curr_len+1)
                    dfs(st+1, False, 0)
            else: # got an 1
                mxl=max(mxl, curr_len+1)
                dfs(st+1, flipped, curr_len+1)


        dfs(0, False, 0)
        return mxl