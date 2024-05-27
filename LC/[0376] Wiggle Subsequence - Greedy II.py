class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N=len(nums)
        dir=-2
        cnt=1
        for ii in range(1, N):
            prev_dir=dir
            if nums[ii] > nums[ii-1]:
                dir=1
            elif nums[ii] < nums[ii-1]:
                dir=-1 

            if dir != prev_dir:
                cnt+=1        

        return cnt