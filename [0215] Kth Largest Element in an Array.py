from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        : O(N) - Avg -> quick select
               - bucket sort
        """

        def quick_select(st, ed, k):
            pivot=nums[st+(ed-st)//2]

            ii, jj, kk = st, st, ed
                if nums[jj] > pivot:
                    nums[jj], nums[kk] = nums[kk], nums[jj]
                    kk -= 1
                elif nums[jj]==pivot:
                    jj +=1
                else:
                    nums[ii], nums[jj] = nums[jj], nums[ii]
                    ii+=1
                    jj+=1

            """
            S S S S P P P P P L L L L
            st      i       k j     ed
            """
            if ed-kk >= k:
                return quick_select(jj, ed, k)
            elif ed-ii+1 >= k:
                return pivot
            else:
                return quick_select(st, ii-1, k-(ed-ii+1))



        N=len(nums)
        return quick_select(0, N-1, k)
