class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums)*(len(nums)+1)//2 - sum(nums)

#######################



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        for ii in range(N):
            curr=nums[ii]
            while curr < N and nums[ii] != ii:
                nums[ii]=nums[curr]
                nums[curr]=curr
                curr=nums[ii]


        for ii in range(N):
            if ii != nums[ii]: return ii

        return N

######################
# Sol 2 bit manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acc=0
        for ii in range(len(nums)):
            acc = (acc ^ ii ^ nums[ii])

        acc ^= len(nums)

        return acc
