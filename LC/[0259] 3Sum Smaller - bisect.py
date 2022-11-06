from bisect import bisect_right
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """

        """
        # take dimensions
        N=len(nums)

        # sort nums
        nums.sort() # whenever you see something sorted -> can we use binary search to help?
        cnt=0 #num of triplets with sum less than target
        #print(" nums: ", nums)
        # traverse sorted nums (0~N-2) - need triplets
        for ii, n1 in enumerate(nums[:-2]):
            #print(" --- ii: ", ii)
            for jj, n2 in enumerate(nums[ii+1:-1], ii+1):
                one_sum=target-n1-n2
                if one_sum <= nums[jj+1]: continue  # binary search optimization <<<<<<< learn this
                #binary search first index that has n3 > one_sum
                """
                one_sum=4
                0  1 2 3 4
                ll 1 2 3 idx 5 6
                """
                idx=bisect_left(nums, one_sum, jj+1)
                cnt += (idx-jj-1)
                #print("one_sum: ", one_sum, " idx: ", idx, "jj: ", jj, " cnt: ", cnt)

        return cnt
