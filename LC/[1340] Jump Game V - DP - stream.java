class Solution {
    public int maxJumps(int[] arr, int d) {
        //get size
        int N=arr.length;

        //declear/initialize dp with 1 (current idx is 1)

        /* [Java][initialize array with same value]
          int[] dp = new int[N];
          Arrays.fill(dp, 1);
        */

        var dp = IntStream.range(0, N) //[Java][stream][initialize array]
                          .map(ii -> 1)
                          .toArray();
        
        //sort arr index with array value
        int[] idx = IntStream.range(0, N) //[java][sort][decending]
                     .boxed()
                     .sorted(Comparator.comparingInt((Integer ii) -> arr[ii]).reversed())
                     .mapToInt(Integer::intValue)
                     .toArray();
        
        //We want to start from the highest and update all dp the highest index can jump to
        for(int ii=0; ii<N; ++ii){//for each idx from top, where we can jump to from the idx and update the dp?
            var idx_ii=idx[ii];
            //jumping right
            for(int jj=idx_ii+1; jj<=Math.min(idx_ii+d, N-1); ++jj){
                if(arr[jj] >= arr[idx_ii]) break;
                dp[jj] = Math.max(dp[jj], dp[idx_ii]+1);
            }
            //jumping left
            for(int jj=idx_ii-1; jj>=Math.max(idx_ii-d, 0); --jj){
                if(arr[jj] >= arr[idx_ii]) break;
                dp[jj] = Math.max(dp[jj], dp[idx_ii]+1);
            }
        }

        //return max of dp
        return Arrays.stream(dp).max().getAsInt(); //[java][steam][array][max]
    }
}