class Solution {

    public int findTargetSumWays(int[] nums, int target) {
        int N = nums.length;
        int[][] dp = new int[25][2005];

        //insert dummy @ beginning of the nums
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());
        list.add(0, 0);
        nums=list.stream().mapToInt(Integer::intValue).toArray();

        int offset=1000;
        //initialize dp
        dp[0][0+offset]=1;
        for(int ii=1; ii<=N; ++ii){ //[1:N]
            for(int jj=-1000; jj<=1000; ++jj){//[-1000, 1000]
                //take positive
                if(jj-nums[ii] >=-1000 && jj-nums[ii]<=1000){
                    dp[ii][jj+offset] += dp[ii-1][jj-nums[ii]+offset];
                }
                //take negative
                if(jj+nums[ii] >=-1000 && jj+nums[ii]<=1000){
                    dp[ii][jj+offset] += dp[ii-1][jj+nums[ii]+offset];
                }
            }

        }
        
        return dp[N][target+offset];
    }
}