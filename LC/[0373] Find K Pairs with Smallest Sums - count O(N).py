class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        mm: the kth smallest sum
        """
        M = len(nums1)
        N = len(nums2)
        ll, rr, ans = nums1[0]+nums2[0], nums1[-1] + \
            nums2[-1], nums1[-1]+nums2[-1]

        def count(mm):
            cnt = 0
            jj = N-1
            for ii in range(M):
                while jj >= 0 and nums1[ii]+nums2[jj] > mm:
                    jj -= 1
                cnt += (jj+1)

            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        # ans is the kth smallest sum
        # print("ans: ", ans)
        res = []
        for a in nums1:
            for b in nums2:
                if a+b <= ans:
                    res.append([a, b])
                else:
                    break

        res.sort(key=lambda x: (x[0]+x[1]))

        return res[:k]
