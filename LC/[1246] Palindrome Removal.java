class Solution {
    public int minimumMoves(int[] arr) {
        //handle edge cases
        int N=arr.length;
        
        if(N==1) return 1;

/**
        //convert int array to Integer Array List
        List<Integer> list = IntStream.of(nums).boxed().collect(Collectors.toCollection(ArrayList::new));
        //insert dummy in the beginning of nums
        list.add(0, 0);
 */

        //var tmp = IntStream.of(arr).boxed().collect(Collectors.toCollection(ArrayList::new)).add(0, 0);


        var arr2 = new ArrayList<Integer>();
        //java insert dummy to array
        arr2.add(0);
        arr2.addAll(Arrays.stream(arr).boxed().collect(Collectors.toList()));
        arr=arr2.stream().mapToInt(i->i).toArray();

        int[][] dp = new int[N+2][N+2];
 
  
        //initialize dp
        for(int len = 1; len<=N; ++len){
            for(int ii=1; ii+len-1<=N; ++ii){//beginning index
                int jj=ii+len-1; //ending index
                dp[ii][jj] = Integer.MAX_VALUE;
                for(int kk=ii; kk<=jj; ++kk){//partitioning the interval,kk is the partition point
                    if(arr[kk]==arr[jj]){
                        /* -- how do you transition from big interval to smaller interval
                        partition range [ii, jj] to [ii, kk-1][kk, jj]
                        */

                        dp[ii][jj] = Math.min(dp[ii][jj], dp[ii][kk-1]+ Math.max(1,dp[kk+1][jj-1]));
                        //dp[ii][jj] = Math.min(dp[ii][jj], dp[ii][kk-1]+ dp[kk+1][jj-1]);
                    }
                }
            }
        }
        return dp[1][N];
    }
}