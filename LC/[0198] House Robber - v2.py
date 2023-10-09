class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        current state only relating to prev state

        ii   r  nr
        0

        """
        N = len(nums)
        rob = 0
        no_rob = 0
        for ii in range(N):
            if ii == 0:
                rob = nums[ii]
                no_rob = 0
                dp = nums[ii]
                continue
            rob_tmp = rob
            no_rob_tmp = no_rob

            rob = nums[ii] + no_rob_tmp
            no_rob = max(rob_tmp, no_rob_tmp)

        return max(rob, no_rob)
