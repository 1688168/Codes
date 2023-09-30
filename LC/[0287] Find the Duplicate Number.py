class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = [0] + nums
        N = len(nums)
        for ii in range(1, N):
            while nums[ii] != ii and nums[ii] < N and nums[ii] != nums[nums[ii]]:
                # Notice this kind of swap not working in Python.  Nums[ii] seems got assigned during the operation
                # nums[ii], nums[nums[ii]] = nums[nums[ii]], nums[ii]
                tmp = nums[ii]
                nums[ii] = nums[tmp]
                nums[tmp] = tmp
        for ii in range(1, N):
            if nums[ii] != ii:
                return nums[ii]
        return -1
