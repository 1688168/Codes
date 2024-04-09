####################
# 20240409
####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        """

        tke = nums[0]  # max profit ending @ house ii
        ntk = 0
        for ii, nn in enumerate(nums[1:], 1):
            tmp_tke = tke
            tmp_ntk = ntk

            tke = nums[ii]+tmp_ntk
            ntk = max(tmp_tke, tmp_ntk)

        return max(tke, ntk)

####################
##### 20231008 #####
####################


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

                continue
            rob_tmp = rob
            no_rob_tmp = no_rob

            rob = nums[ii] + no_rob_tmp
            no_rob = max(rob_tmp, no_rob_tmp)

        return max(rob, no_rob)
