class Solution {

    private Pair<Integer, Integer> count(final String x){
        int zz=0;
        int oo=0;

        for(int ii=0; ii< x.length(); ++ii){
            if('0'==x.charAt(ii)){
                zz +=1;
            }else{
                oo +=1;
            }
        }

        return new Pair<Integer, Integer>(zz, oo);
    }

    public int findMaxForm(String[] strs, int m, int n) {
        final int N = strs.length;

        int[][][] dp = new int[N][m+1][n+1];

        List<Pair<Integer, Integer>> counts = Arrays.stream(strs) //to stream of String
        .map(x -> count(x)) //converting to list of pairs
        .collect(Collectors.toList()); //a list of Pairs (zeros, ones)

        //populate dp
        for(int ii=0; ii<N; ++ii){ //[0, N-1]
            int z=counts.get(ii).getKey().intValue();
            int o=counts.get(ii).getValue().intValue();
            for(int jj=0; jj<=m; ++jj){ //[0, m]
                for(int kk=0; kk<=n; ++kk) //[0, n]
                    if(ii==0){
                        //skip do nothing as already zero
                        //take
                        if(jj>=z && kk>=o) dp[ii][jj][kk] = 1;
                    }else{
                        //skip
                         dp[ii][jj][kk] = Math.max(dp[ii][jj][kk], dp[ii-1][jj][kk]);
                        //take
                        if(jj-z >=0 && kk-o >=0){
                            dp[ii][jj][kk] = Math.max(dp[ii][jj][kk], dp[ii-1][jj-z][kk-o]+1);
                        } 
                    }
            }
        }
        return dp[N-1][m][n];
    }
}