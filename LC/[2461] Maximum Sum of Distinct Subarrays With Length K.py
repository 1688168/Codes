############
# 20230917
############

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        - x x x x x
        - define a sliding window with size k
        - maintain a set to carry distinct numbers
        - if size of set same as k -> all elements are distinct
        - calculate subarray sum by prepare prefix sum 
        """
        N = len(nums)

        val2cnt = {}
        ans = 0
        ttl = 0
        for ii, vv in enumerate(nums):
            val2cnt[vv] = val2cnt.get(vv, 0) + 1

            if ii < k:
                ttl += vv
                if len(val2cnt) == k:
                    ans = ttl
                continue

            pv = nums[ii-k]
            ttl = ttl+vv-pv

            val2cnt[pv] -= 1
            if val2cnt[pv] == 0:
                del val2cnt[pv]

            if len(val2cnt) == k:
                ans = max(ans, ttl)
        return ans


############
# 20230917
############
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        - x x x x x
        - define a sliding window with size k
        - maintain a set to carry distinct numbers
        - if size of set same as k -> all elements are distinct
        - calculate subarray sum by prepare prefix sum 
        """
        N = len(nums)
        presum = [0]*N

        for ii in range(N):
            if ii == 0:
                presum[ii] = nums[ii]
            else:
                presum[ii] = presum[ii-1]+nums[ii]

        val2cnt = {}
        ans = 0
        for ii, vv in enumerate(nums):

            val2cnt[vv] = val2cnt.get(vv, 0) + 1

            if ii < k:
                ttl = presum[ii] - (presum[ii-k] if ii >= k else 0)
                if len(val2cnt) == k:
                    ans = ttl
                continue

            pv = nums[ii-k]

            val2cnt[pv] -= 1
            if val2cnt[pv] == 0:
                del val2cnt[pv]

            if len(val2cnt) == k:
                ttl = presum[ii] - (presum[ii-k] if ii >= k else 0)
                ans = max(ans, ttl)
        return ans


#############################################


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N < k:
            return 0
        mxs = float('-inf')

        ss = Counter(nums[:k])
        presum = []
        for ii, vv in enumerate(nums):
            if ii == 0:
                presum.append(nums[ii])
            else:
                presum.append(nums[ii]+presum[-1])
        # print("presum: ", presum)
        # print("start  ii: ", ii)
        ii = k-1
        while ii < N:
            # print(ss)
            if len(ss) == k:
                # print("ii: ", ii, " ii+1-k: ", ii+1-k)
                # mxs=max(mxs, sum(nums[ii+1-k:ii+1]))
                mxs = max(mxs, presum[ii]-(presum[ii-k] if ii >= k else 0))

            ss[nums[ii+1-k]] -= 1
            if ss[nums[ii+1-k]] == 0:
                del ss[nums[ii+1-k]]

            if ii+1 < N:
                ss[nums[ii+1]] = ss.get(nums[ii+1], 0) + 1
            # if nums[ii+1-k] in ss:
            #     ss.remove(nums[ii+1-k])
            # if ii+1 < N:
            #     ss.add(nums[ii+1])
            ii += 1
            # print(" mxs: ", mxs, " ss: ", ss)
        return mxs if mxs != float('-inf') else 0
