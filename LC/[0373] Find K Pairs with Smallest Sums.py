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
            for n in nums1:
                if n >= mm:
                    break
                idx = bisect.bisect_right(nums2, mm-n)
                cnt += idx
            print(" count: ", cnt)
            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2
            print(" ll: ", ll, " rr: ", rr, " mm: ", mm)
            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        # ans is the kth smallest sum
        print("ans: ", ans)
        res = []
        for a in nums1:
            if a >= ans:
                break
            for b in nums2:
                if a+b > ans:
                    break
                if a+b <= ans:
                    res.append([a, b])
                    if len(res) >= k:
                        break
            if len(res) >= k:
                break
        res.sort()
        return res
