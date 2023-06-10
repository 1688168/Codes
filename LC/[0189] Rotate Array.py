class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # reverse 0~N-k
        # reverse N-k~N
        # reverse all
        N=len(nums)
        k=k%N
        ll, rr = 0, N-k
        nums[:N-k] = reversed(nums[:N-k])
        nums[N-k:] = reversed(nums[N-k:])
        nums.reverse()
