class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ii, jj, kk = m-1, n-1, m+n-1

        while ii >= 0 and jj >= 0:
            if nums1[ii] >= nums2[jj]:
                nums1[kk] = nums1[ii]
                ii-=1
            else:
                nums1[kk] = nums2[jj]
                jj-=1
            
            kk-=1
        
        while ii>=0:
            nums1[kk]=nums1[ii]
            ii-=1
            kk-=1

        while jj>=0:
            nums1[kk]=nums2[jj]
            jj-=1
            kk-=1
