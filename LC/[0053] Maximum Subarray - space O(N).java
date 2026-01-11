class Solution {
    public int maxSubArray(int[] nums) {
        //take dimension
        int N = nums.length;

        //insert dummy into nums
        //java, insert dummy to beginning of int array via stream
        nums = IntStream.concat(IntStream.of(0), IntStream.of(nums))
                                .toArray();
        
        //declare dp
        //java declare int array and initialize to 0
        var dp = IntStream.range(0, N+1).map(ii -> Integer.MIN_VALUE/2).toArray();
        

        //initialize the array
        for(int ii=1; ii<=N; ++ii){
            dp[ii] = Math.max(nums[ii], nums[ii]+dp[ii-1]);
        }

        //java stream return max in in an array
        return Arrays.stream(dp)
                        .max()
                        .orElseThrow(); 

    }
}

/*
# Analysis: 
* N=10^5
* Largest subarray sum -> Kadane
# Bruteforce:
* all subarray: N^2+N -> 10^10
# Greedy:
# DP: build overall solution from repeating sub-problems
* single array, current state can be derived from previous state
*  base case: dp[0] = min(sum(nums[:1]), 0) * empty array is NOT a valid subarray
* nums[:2] = max(nums[ii]+dp[ii-1], nums[ii], 0)
* let dp[ii] be the max subarray sum for nums[:ii+1]
      dp[ii] = max(nums[ii], nums[ii]+dp[ii-1], 0)
* return max(dp)
*/