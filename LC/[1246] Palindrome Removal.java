class Solution {
    public int minimumMoves(int[] arr) {
        //handle edge cases
        int N=arr.length;
        
        if(N==1) return 1;
        //Java insert dummy in the beginning of the array
        //stream->list->insert->array

        //convert int array to Integer Array List
        List<Integer> list = IntStream.of(arr).boxed().collect(Collectors.toCollection(ArrayList::new));
        list.add(0, 0);
        arr=list.stream().mapToInt(ii->ii).toArray();

        int[][] dp = new int[N+2][N+2];
 
        //initialize dp
        for(int len = 1; len<=N; ++len){
            for(int ii=1; ii+len-1<=N; ++ii){//beginning index
                int jj=ii+len-1; //ending index
                dp[ii][jj] = Integer.MAX_VALUE;
                for(int kk=ii; kk<=jj; ++kk){//try each kk in [ii:jj-1] and see if we can eliminate both in one shot
                    if(arr[kk]==arr[jj]){ //worst case kk==jj -> arr[kk]==arr[jj] -> remove the last one
                        dp[ii][jj] = Math.min(dp[ii][jj], dp[ii][kk-1]+ Math.max(1,dp[kk+1][jj-1]));
                    }
                }
            }
        }
        return dp[1][N];
    }
}