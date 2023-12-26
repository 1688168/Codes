##############
# 20231112
##############
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        median:
        odd:
            len//2 (index)
        even:
            (len//2+len//2+1)/2
        """
        M = len(nums1)
        N = len(nums2)

        def get_kth_element(nums1, s1, M, nums2, s2, N, kk):
            if M > N:
                return get_kth_element(nums2, s2, N, nums1, s1, M, kk)
            if M == 0:
                return nums2[s2+kk-1]

            if kk == 1:
                return min(nums1[s1], nums2[s2])
            k1 = min(M, kk//2)
            k2 = kk-k1

            if nums1[s1+k1-1] < nums2[s2+k2-1]:
                return get_kth_element(nums1, s1+k1, M-k1, nums2, s2, N, kk-k1)
            else:
                return get_kth_element(nums1, s1, M, nums2, s2+k2, N-k2, kk-k2)

        if (M+N) % 2 == 1:  # odd case
            # kth element (last element is not index)
            return get_kth_element(nums1, 0,  M, nums2, 0, N, (M+N)//2+1)
        else:  # even case
            # kth element (last element is not index)
            kth = get_kth_element(nums1, 0, M, nums2, 0, N, (M+N)//2)
            # kth element (last element is not index)
            kthPlusOne = get_kth_element(nums1, 0, M, nums2, 0, N, (M+N)//2+1)
            return (kth+kthPlusOne)/2

########################
########################


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
