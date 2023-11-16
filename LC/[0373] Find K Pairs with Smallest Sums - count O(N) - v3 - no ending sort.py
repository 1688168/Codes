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
            ii = 0
            jj = N-1
            while ii < M and jj >= 0:
                if nums1[ii]+nums2[jj] > mm:
                    jj -= 1
                else:
                    cnt += (jj+1)
                    ii += 1
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
        res_equal = []
        for a in nums1:
            for b in nums2:
                if a+b < ans:
                    res.append([a, b])
                elif a+b == ans:
                    res_equal.append([a, b])
                else:
                    break

        if len(res) < k:
            for jj in range(len(res_equal)):
                if len(res) < k:
                    res.append(res_equal[jj])
                else:
                    break
        # res.sort(key=lambda x: (x[0]+x[1]))

        return res[:k]
