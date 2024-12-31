/*
* partition nums into k (non-empty) sub-arrays -> max score
* where score = sum of avg of subarrays
* -> find optimized solution from partition nums into k -> DP IV
*/
class Solution {
    public double largestSumOfAverages(int[] nums, int k) {
        int N = nums.length;
        double[][] dp = new double[N+1][k+1];
        //dp[ii][kk]: max score for nums[:ii+1], k=kk
        //dp[ii][kk] = max(dp[ii][kk], avg(nums[jj:ii+1]+dp[ii-1][jj-1]))
        for(int ii=0; ii<=N; ++ii){
            for(int jj=0; jj<=k; ++jj) dp[ii][jj] = Integer.MIN_VALUE;
        }
        dp[0][0] = 0.0; //nums=None, no partion -> max score=0
        
        //java insert dummy to beginning of int array
        /*
        1. Java convert int array to List of Integers
        2. Java insert element into List
        3. Java convert List of Integer to int array
        */
        var list = IntStream.of(nums).boxed().collect(Collectors.toCollection(ArrayList::new));
        list.add(0, 0);
        //java map list Integer to int
        nums = list.stream().mapToInt(ii->ii).toArray();//java inserted dummy int to beginning of an array

        for(int ii=1; ii<=N; ++ii){//ii=0 is the dummy.  For each element as last element in last partition
            for(int kk=1; kk<=Math.min(k, ii); ++kk){//from 1 partition to k partition.
                double ss = 0;
                for(int jj=ii; jj>=kk; --jj){//jj is the starting index of last partition.
                    ss += nums[jj];
                    dp[ii][kk] = Math.max(dp[ii][kk], ss/(ii-jj+1)+dp[jj-1][kk-1]);
                }
            }

        }

        double ans = 0;
        for(int kk=1; kk<=k; ++kk) ans = Math.max(ans, dp[N][kk]);

        return ans;
    }
}