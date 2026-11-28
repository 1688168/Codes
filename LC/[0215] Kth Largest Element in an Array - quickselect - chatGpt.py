from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(st, ed, target):
            if st == ed:
                return nums[st]

            pivot = nums[st + (ed - st) // 2]

            ii, jj, kk = st, st, ed

            while jj <= kk:
                if nums[jj] > pivot:
                    nums[jj], nums[kk] = nums[kk], nums[jj]
                    kk -= 1
                elif nums[jj] == pivot:
                    jj += 1
                else:
                    nums[ii], nums[jj] = nums[jj], nums[ii]
                    ii += 1
                    jj += 1

            # [st, ii)     < pivot
            # [ii, jj)     == pivot
            # [jj, ed + 1) > pivot

            if target < ii:
                return quick_select(st, ii - 1, target)
            elif target < jj:
                return pivot
            else:
                return quick_select(jj, ed, target)

        return quick_select(0, len(nums) - 1, len(nums) - k)