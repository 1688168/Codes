import bisect
from functools import lru_cache
class Solution:


def lengthOfLIS_binary(self, nums):
    res = []
    for x in nums:
        idx = bisect.bisect_left(res, x)
        # print("idx: ", idx, " x: ", x, " len: ", length, " len(nums): ", len(nums))

        if idx == len(res):
            res.append(x)
        else:
            res[idx] = x
    return len(res)
