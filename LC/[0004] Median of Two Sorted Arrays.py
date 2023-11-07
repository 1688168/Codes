class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)

        def find_kth_smallest(nums1, a, m, nums2, b, n, kk):
            # always ensure nums1 is shorter
            if m > n:
                return find_kth_smallest(nums2, b, n, nums1, a, m, kk)
            if m == 0:
                return nums2[b+kk-1]  # if nums1 is empty, it is the b+kk-1
            if kk == 1:
                return min(nums1[a], nums2[b])  # if kk==1, pick the smallest

            # each side we pick kk//2 elements
            k1 = min(m, kk//2)  # m could be shorter than kk
            k2 = kk-k1

            if nums1[a+k1-1] < nums2[b+k2-1]:
                return find_kth_smallest(nums1, a+k1, m-k1, nums2, b, n, kk-k1)
            else:
                return find_kth_smallest(nums1, a, m, nums2, b+k2, n-k2, kk-k2)

        # length is odd or even
        if ((M+N) % 2) == 1:
            # kk is length, not idx
            return find_kth_smallest(nums1, 0, M, nums2, 0, N, (M+N+1)//2)
        else:
            return (find_kth_smallest(nums1, 0, M, nums2, 0, N,
                                      (M+N)//2)+find_kth_smallest(nums1, 0, M, nums2, 0, N, (M+N)//2+1))/2  # please notice here is taking float divison
