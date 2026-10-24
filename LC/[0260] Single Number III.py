class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for nn in nums: xor^=nn

        # the first bit that is 1
        mask = xor&(-xor)

        a=b=0
        for nn in nums:
            if nn & mask:
                a ^= nn
            else:
                b ^= nn

        return [a, b]

"""
# 3 key bits operations
1. a^b=0 if a==b
2. x&(x-1) -> remove the last 1 bit
3. x&(-x) -> isolate the last 1 bit
"""

        