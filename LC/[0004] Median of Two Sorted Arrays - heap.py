from heapq import heappush, heappop, heappushpop


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1. odd or even
        2. if odd, find k=(M+N+1)//2
        3. if even, find: k1=(M+N+1)//2, k2=k1+1, return the avg of these two
        """
        M = len(nums1)
        N = len(nums2)

        def find_kth_element(nums1, nums2, kk):
            mnq = []
            ii, jj = 0, 0
            m = len(nums1)
            n = len(nums2)

            if m > n:  # ensures len(nums1) < len(nums2)
                return find_kth_element(nums2, nums1, kk)

            if m == 0:
                return nums2[kk]  # kk is index

            heappush(mnq, (nums1[0], 1))
            heappush(mnq, (nums2[0], 2))
            ii = jj = 1
            cnt = 0

            while mnq and cnt <= kk:  # we need to take k element out [0, k-1]
                curr, idx = heappop(mnq)

                cnt += 1
                if idx == 1 and ii < m:  # even we have no more element to add into the mnq, we still need to continue to fetch
                    heappush(mnq, (nums1[ii], 1))
                    ii += 1
                elif jj < n:
                    heappush(mnq, (nums2[jj], 2))
                    jj += 1

            return curr

        # for median, we always need to consider odd/even cases.  basically, we need to be able to find kth element
        # kth element, idx=k-1
        if (M+N) % 2 == 1:
            kk = (M+N)//2  # kk is index
            return find_kth_element(nums1, nums2, kk)
        else:
            kk = (M+N)//2-1  # 0 1 2 3: idx=(1, 2)
            return (find_kth_element(nums1, nums2, kk)+find_kth_element(nums1, nums2, kk+1))/2
