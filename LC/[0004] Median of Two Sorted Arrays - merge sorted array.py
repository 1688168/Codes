class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        def get_kth(nums1, m, s1, nums2, n, s2, k):
            if m > n:
                return get_kth(nums2, n, s2, nums1, m, s1, k)
            if m == 0:
                return nums2[s2+k-1]
            if k == 1:
                return min(nums1[s1], nums2[s2])

            ii, jj = s1, s2
            cnt = 0
            # tmp=[]
            ans = None
            while ii < m or jj < n:
                if jj >= n or (ii < m and nums1[ii] < nums2[jj]):
                    # tmp.append(nums1[ii])
                    ans = nums1[ii]
                    ii += 1
                else:
                    # tmp.append(nums2[jj])
                    ans = nums2[jj]
                    jj += 1

                cnt += 1
                if cnt == k:
                    break
            return ans

        if (m+n) % 2 == 1:
            return get_kth(nums1, m, 0, nums2, n, 0, (m+n)//2+1)
        else:
            a = get_kth(nums1, m, 0, nums2, n, 0, (m+n)//2)
            b = get_kth(nums1, m, 0, nums2, n, 0, (m+n)//2+1)
            return (a+b)/2
