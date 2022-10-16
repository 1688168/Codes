class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        N=len(nums)
        for ii in range(N):
            curr=nums[ii]
            nn=int(str(curr)[::-1])
            nums.append(nn)

        #print(nums)
        s=set(nums)

        return len(s)
        
