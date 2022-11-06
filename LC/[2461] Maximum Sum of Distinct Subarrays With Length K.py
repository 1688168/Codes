from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N=len(nums)
        if N < k: return 0
        mxs=float('-inf')


        ss=Counter(nums[:k])
        presum=[]
        for ii, vv in enumerate(nums):
            if ii==0:
                presum.append(nums[ii])
            else:
                presum.append(nums[ii]+presum[-1])
        #print("presum: ", presum)
        #print("start  ii: ", ii)
        ii=k-1
        while ii < N:
            #print(ss)
            if len(ss)==k:
                #print("ii: ", ii, " ii+1-k: ", ii+1-k)
                #mxs=max(mxs, sum(nums[ii+1-k:ii+1]))
                mxs=max(mxs, presum[ii]-(presum[ii-k] if ii >= k else 0))

            ss[nums[ii+1-k]] -= 1
            if ss[nums[ii+1-k]]==0:
                del ss[nums[ii+1-k]]

            if ii+1 < N:
                ss[nums[ii+1]] = ss.get(nums[ii+1], 0) +1
            # if nums[ii+1-k] in ss:
            #     ss.remove(nums[ii+1-k])
            # if ii+1 < N:
            #     ss.add(nums[ii+1])
            ii+=1
            #print(" mxs: ", mxs, " ss: ", ss)
        return mxs if mxs!=float('-inf') else 0
