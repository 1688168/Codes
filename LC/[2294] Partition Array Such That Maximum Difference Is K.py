class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        : nums: postive/negative
        : k: -1, 1
        : subsequence
        : Return the minimum number of subsequences needed such that
        : => the difference between the maximum and minimum values in each subsequence is at most k.
        : nums: 3, 6, 1, 2, 5
        : k=2
        : min num of subsequences
        : max length of sub-sequences with range <= k
        : max increasing sub-sequence: Kadane
        : dp[ii] =min number of subsequences ending @ ii where conform all subsequences are with range <= k
        : x x x x x x x x
        :       i
        :   a         b
        """
        # subsequence
        nums.sort()
        ll, rr, N = 0, 0, len(nums)
        curr_min=nums[0] #nums.length >= 1

        cnt=1
        for rr in range(N):
            if nums[rr]-curr_min > k:
                cnt += 1
                curr_min=nums[rr]

            curr_min_so_far=min(curr_min, nums[rr])

        return cnt

            
