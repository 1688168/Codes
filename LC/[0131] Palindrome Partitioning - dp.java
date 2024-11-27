/*
* *return all possible results -> search for all
* * 
*/

class Solution {
    private final int MAX_LEN=16;
    private List<List<String>> res = new ArrayList<List<String>>();//java two dimensional ArrayList
    private boolean[][] dp = new boolean[MAX_LEN][MAX_LEN];
    private Boolean isPalindrome(int st, int ed){
        return dp[st][ed];
    }
    private void buildIsPalindrome(String ss){
        //single char is true
        int N=ss.length();
        for(int ii=0; ii< N; ++ii) dp[ii][ii]=true;
        for(int ii=0; ii< N-1; ++ii){
            if(ss.charAt(ii)==ss.charAt(ii+1)) dp[ii][ii+1]=true;
        }

        for(int len=3; len <= N; ++len){
            for(int ii=0; ii+len-1< N; ++ii){
                int jj = ii+len-1;
                dp[ii][jj]= false;
                if(ss.charAt(ii)==ss.charAt(jj)){
                    dp[ii][jj] = dp[ii+1][jj-1];
                }
            }
        }

    }
    private void partition(String s, int st, List<String> path){
        int N = s.length();
        if(st>=N){
            res.add(path);
            return;
        }

        for(int ii=st; ii<N; ++ii){
            if(isPalindrome(st, ii)){
                String ss=s.substring(st, ii+1);
                //java concatenate two lists
                partition(s, ii+1, Stream.concat(path.stream(),List.of(ss).stream()).collect(Collectors.toList()));
            }
        }

        return;
    }
    public List<List<String>> partition(String s) {
        buildIsPalindrome(s);
        List<String> path = new ArrayList<String>();
        partition(s, 0, path);
        
        return res;
    }
}