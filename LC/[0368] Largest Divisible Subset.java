class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int N = nums.length;
        Arrays.sort(nums);
        //define DP:
        // dp[ii]: max subset count s.t. satisfy the divisible requirement
        // dp[ii] = dp[jj] + 1 if nums[ii]
        var dp =  IntStream.range(0, N)
                           .map(ii -> 1) //min is 1 (self divisible by self)
                           .toArray();
        var prev = IntStream.range(0, N)
                           .map(ii -> -1) //min is 1 (self divisible by self)
                           .toArray();

        //when ii=0 -> already initialized to 1
        for(int ii=1; ii<N; ++ii){
            for(int jj=0; jj<ii; ++jj){
                if(nums[ii]%nums[jj]==0){
                    if(dp[jj]+1 > dp[ii]){
                        dp[ii] = dp[jj]+1;
                        prev[ii]=jj;
                    }
                }
            }
        }

        //find the max divisible subset
        int mx=-1;
        int mx_idx = -1;
        for(int ii=0; ii<N; ++ii){
            if(dp[ii]>mx){
                mx=dp[ii];
                mx_idx=ii;
            }
            
        }
        
        List<Integer> ans = new ArrayList<>();
        while(mx_idx != -1){
            ans.add(nums[mx_idx]);
            mx_idx = prev[mx_idx];
        }
        return ans;
 
    }
}

// * nums: distinct positive int
// * N=1000 -> N^2 
// -> Largest subset answer. 
// * we don't have obvious heuristic to group the elements.
// * largest subset -> order does not matter
// * N^2. DP2 <<<

// * bruteforce: 2^N grouping. filter out groups satisfy the requirement, return the largest.

// * when asking about subset -> order doesn't matter -> highly likely we need to sort
// * current ii is divisible by prev @jj -> longest divisible subsequence (after sorting)
// * asking the path (record previous)
// 1. sort nlogn. 
// 2. dp[ii]: 

