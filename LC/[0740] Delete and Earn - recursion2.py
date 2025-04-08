class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # current state is affected by prevStateValue + 1, prevStateValue -1
        # since sorting the array doesn't change the result. -> sort
        # after sorting the array. currentState dp[ii] is affected by nums[ii-1]+1
        N = len(nums)
        nums.sort() # sort the array
        print(nums)
        def hp(st, prev, currMXP):
            #print(f"st={st}, prev={prev}, currMXP={currMXP}")
            if st >=N: 
                return currMXP
           

            # ntke
            ntk = hp(st+1, prev, currMXP)

            # tke
            tke=0
            if prev == -1 or nums[st] != prev+1:
                tke = hp(st+1, nums[st], currMXP+nums[st])
            
            return max(ntk, tke)


        return hp(0, -1, 0) 