##############
# 20231217
##############
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N = m+n
        ii = N-1
        jj = m-1
        kk = n-1
        while jj >= 0 and kk >= 0:
            if nums1[jj] >= nums2[kk]:
                nums1[ii] = nums1[jj]
                jj -= 1
            else:
                nums1[ii] = nums2[kk]
                kk -= 1
            ii -= 1

        while kk >= 0:
            nums1[ii] = nums2[kk]
            ii -= 1
            kk -= 1

        return


########################

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i1, i2 = m-1, n-1
        for ii in reversed(range(m+n)):

            if i1 >= 0 and i2 >= 0:
                if nums1[i1] > nums2[i2]:
                    nums1[ii] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[ii] = nums2[i2]
                    i2 -= 1
            elif i1 >= 0:
                nums1[ii] = nums1[i1]
                i1 -= 1
            elif i2 >= 0:
                nums1[ii] = nums2[i2]
                i2 -= 1

        return
