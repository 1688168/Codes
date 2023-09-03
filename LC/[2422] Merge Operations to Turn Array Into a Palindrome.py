"""
https://youtu.be/rz3YGaJII44
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        cnt = 0
        ll, rr = 0, N-1
        left = nums[ll]
        right = nums[rr]

        while ll < rr:
            # print(" left: ", left, " right: ", right, " ll: ", ll, " rr: ", rr, " cnt: ", cnt)
            if left == right:
                ll += 1
                rr -= 1
                left += nums[ll]
                right += nums[rr]
                continue

            """
            L L L L R R R R
            """

            if left > right:
                cnt += 1
                rr -= 1
                right += nums[rr]

                continue

            if left < right:
                cnt += 1
                ll += 1
                left += nums[ll]

                continue

        return cnt
