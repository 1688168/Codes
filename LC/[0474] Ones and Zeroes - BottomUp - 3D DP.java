class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        final int N = strs.length;

        int[][][] dp = new int[N][m+1][n+1];
        int[] zz = new int[N];
        int[] oo = new int[N];

        //populate zz/oo => can you change this to stream implementation
        for(int ii=0; ii<N; ++ii){
            String ss = strs[ii];
            int z=0;
            int o=0;
            for(int jj=0; jj<ss.length(); ++jj){
                char cc=ss.charAt(jj);
                if(cc=='0'){
                    ++z;
                }else{
                    ++o;
                }
            }   
            zz[ii]=z;
            oo[ii]=o;
        }

        //populate dp
        for(int ii=0; ii<N; ++ii){ //[0, N-1]
            int z=zz[ii];
            int o=oo[ii];
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