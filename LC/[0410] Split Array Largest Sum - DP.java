class Solution {
    public int splitArray(int[] nums, int k) {
        int N = nums.length;

        //initialize DP
        int[][] dp = IntStream.range(0, N+1)
                              .mapToObj(ii->IntStream.range(0, k+1).map(jj -> Integer.MAX_VALUE).toArray())
                              .toArray(int[][]::new);
        dp[0][0]=0;

        //java convert int array to List of Integers
        //java insert dummy to the beginning of an array
        List<Integer> list = IntStream.of(nums).boxed().collect(Collectors.toCollection(ArrayList::new));
        list.add(0, 0);
        nums=list.stream().mapToInt(i -> i).toArray();//java convert list to int array

        for(int ii = 1; ii<=N; ++ii){//for each element
            for(int jj=1; jj<=Math.min(k, ii); ++jj){ //for each partition num
                int ss=0;
                for(int kk=ii; kk>=jj; --kk){ //go last partition interval (kk, ii)
                    ss+=nums[kk];
                    dp[ii][jj] = Math.min(dp[ii][jj], Math.max(dp[kk-1][jj-1], ss));
                }
            }
        }
        return dp[N][k];  
    }
}