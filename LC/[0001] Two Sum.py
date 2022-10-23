class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        : all combination N^2
        : use a map to cache all that is visited for complement lookup
        """

        val2idx={}

        for ii, vv in enumerate(nums):
            if target-nums[ii] in val2idx:
                return (val2idx[target-nums[ii]], ii)
            else:
                val2idx[vv]=ii


        return None # shouldn't be here
