class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N=len(nums)

        def hp(st, nums, state, tke, ntk):
            #print(state)
            #print(f"st=[{st}], N=[{N}], tke=[{tke}], ntk=[{ntk}] ----- ")

            if st >= N: return max(tke, ntk)


            if state[st] != -1: #cannot take
                return hp(st+1, nums, state[:], tke, max(tke, ntk))
            else: # can take
                # but skip
                nntk = hp(st+1, nums, state[:], tke, max(tke, ntk))
                
                for ii in val2idx[nums[st]+1]: state[ii] = st
                for ii in val2idx[nums[st]-1]: state[ii] = st
                state[st] = st
                ttke = hp(st+1, nums, state[:], tke+nums[st], ntk)
                return max(nntk, ttke)

        val2idx=DefaultDict(set)
        for ii, vv in enumerate(nums):
            val2idx[vv].add(ii) #reverse lookup
        
        #print(val2idx)

        dp=[-1 for ii in range(N)] # is deleted @ ii
        return hp(0, nums, dp[:], 0, 0)
        
        