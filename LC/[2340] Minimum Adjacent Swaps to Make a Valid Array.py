class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        N = len(nums)
        rr = N-1
        while rr >= 0 and nums[rr] != mx:
            rr -= 1

        cnt = 0
        while rr+1 < N:
            cnt += 1
            nums[rr], nums[rr+1] = nums[rr+1], nums[rr]
            rr += 1

        ll = 0
        while ll < N and nums[ll] != mn:
            ll += 1

        cnt += ll

        return cnt
