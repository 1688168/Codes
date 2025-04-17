class Solution {
    public int deleteAndEarn(int[] nums) {
        int N = nums.length;

        if(N==0) return 0;
        if(N==1) return nums[0];

        Arrays.sort(nums); //sorting is default to increasing order
        int M = nums[N-1]; //last element in the sorted array is the max

        //converting the input array to array by values
        int[] arr = new int[M+1]; //index is the original value from num.  value is number of repeating values with this original value

        for(var xx: nums) arr[xx] += xx; //populating the transformed array

        //now we transformed the problem to a house robber problem.  each value can be pick or skip depends on state of previous value

        //declare dp to maintain state (single array of initial value as zero - no profit)
        //where dp[ii] = max profit can be achieved @ ii
        var dp = IntStream.range(0, M+1).map(ii -> 0).toArray();
        //initialize dp
        dp[0] = 0; //zero value, profit zero
        dp[1] = arr[1];

        for(int ii=2; ii<=M; ++ii){
            dp[ii] = Math.max(arr[ii]+dp[ii-2], dp[ii-1]);
        }
        
        return dp[M];
    }
}