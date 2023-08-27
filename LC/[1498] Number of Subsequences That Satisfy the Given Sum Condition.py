
M = pow(10, 9) + 7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # for subsequency and Time: nlogn, start from sorting

        N = len(nums)
        rr = N-1
        ans = 0
        # let nums[ii] the min of the subsequence
        for ii, vv in enumerate(nums):
            if vv > target or rr < ii:
                break  # min already greater than target, just break
            _sum = vv + (nums[rr] if rr >= ii else 0)

            while rr > ii and _sum > target:  # if sum is too big, shrink the window
                rr -= 1
                if rr < ii:
                    break
                _sum = vv + (nums[rr] if rr >= ii else 0)
                if _sum <= target:
                    break  # everything in the window counts

            if _sum <= target and rr >= ii:
                ans += pow(2, rr-ii)
                ans %= M
                # print("ii: ", ii, " rr: ", rr, " ans: ", ans)

        return ans
