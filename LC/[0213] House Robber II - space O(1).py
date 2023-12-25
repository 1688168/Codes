class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # rob first
        # -> no rob second
        # -> no rob the last
        dp_rob = nums[0]
        dp_no_rob = nums[0]  # mandatory rob

        for ii in range(N):
            if ii == 0:
                dp_rob = nums[0]
                dp_no_rob = nums[0]
                continue

            if ii == 1:  # since we rob first, 2nd must be no rub
                continue

            if ii == N-1:  # last must be no rub
                continue

            dp_rob_tmp = dp_rob
            dp_no_rob_tmp = dp_no_rob
            dp_rob = nums[ii]+dp_no_rob_tmp
            dp_no_rob = max(dp_rob_tmp, dp_no_rob_tmp)

        mx_rob_first = max(dp_rob, dp_no_rob)

        # not rob first -> all others flexible
        dp_rob = 0
        dp_no_rob = 0

        for ii in range(N):
            if ii == 0:
                dp_rob = 0
                dp_no_rob = 0
                continue

            dp_rob_tmp = dp_rob
            dp_no_rob_tmp = dp_no_rob
            dp_rob = nums[ii]+dp_no_rob_tmp
            dp_no_rob = max(dp_rob_tmp, dp_no_rob_tmp)

        mx_no_rob_first = max(dp_rob, dp_no_rob)

        return max(mx_rob_first, mx_no_rob_first)
