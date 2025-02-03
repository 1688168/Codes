class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int N = jobDifficulty.length;

        //java insert dummy to an Array
        List<Integer> list = IntStream.of(jobDifficulty).boxed().collect(Collectors.toCollection(ArrayList::new));
        list.add(0, 0);
        jobDifficulty=list.stream().mapToInt(i -> i).toArray();//java convert list to int array
        //java create/initialize 2D array from stream 
        int[][] dp = IntStream.range(0, N+1) //[0, 1, 2, ..., N]
            .mapToObj(ii -> IntStream.range(0, d+1).map(jj -> Integer.MAX_VALUE/2).toArray())
            .toArray(int[][]::new);
        
        dp[0][0] = 0; //dummy day, no job, 0 difficulty

        for(int ii=1; ii<=N; ++ii){//up to iith job
            for(int dd=1; dd<=Math.min(d, ii); ++dd){//for each number of 
                int mxd = jobDifficulty[ii];
                for(int jj=ii; jj >= dd; --jj){//jj is the starting idx of last partition
                    mxd=Math.max(mxd, jobDifficulty[jj]);
                    dp[ii][dd] = Math.min(dp[ii][dd], dp[jj-1][dd-1] + mxd);

                }

            }
        }

        if(dp[N][d] >= Integer.MAX_VALUE/2) return -1;

        return dp[N][d];

        
    }
}
/*
Analysis:
* schedule a list of jobs in d days: -> partition an int array into d subarrays
* each day is each sub-array
* min difficulty of a job schedule -> min sum of max value in each sub-array
* partition an array into k non-empty subarray and optimize something -> DP IV

*/