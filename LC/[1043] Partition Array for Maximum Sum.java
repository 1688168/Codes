class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int N = arr.length;

        //[java][stream][insert][dummy][convert array to list][list to array]
        var list = IntStream.of(arr).boxed().collect(Collectors.toCollection(ArrayList::new));
        list.add(0, 0);
        //java map list Integer to int
        arr = list.stream().mapToInt(ii->ii).toArray();//java inserted dummy int to beginning of an array

        //declare DP
        int[] dp = new int[N+1];

        //initialize DP
        for(int ii=0; ii<=N; ++ii){
            dp[ii] = Integer.MIN_VALUE/2;
        }

        dp[0]=0;
        
        //populate DP
        for(int ii=0; ii<=N; ++ii){
            int mx=Integer.MIN_VALUE;
            for(int ss=ii; ss>=Math.max(1, ii-k+1); --ss){
                mx=Math.max(mx, arr[ss]);
                dp[ii] = Math.max(dp[ii], dp[ss-1]+mx*(ii-ss+1));
            }
        }

        return dp[N];
    }
}