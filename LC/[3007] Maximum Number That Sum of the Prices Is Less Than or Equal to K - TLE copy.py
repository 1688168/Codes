from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n2f = Counter(nums)
        fs = [ff for ff in n2f.values()]
        mxf = max(fs)

        ans = 0
        for nn, ff in n2f.items():
            if ff == mxf:
                ans += ff

        return ans
