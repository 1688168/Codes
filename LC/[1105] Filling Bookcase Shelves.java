class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int N = books.length;
        int [] dp = new int[N+1];
        int k = shelfWidth;

        //insert dummy
        int[][] books2 = new int[N+1][2];//each ii is (thickness, height)
        for(int ii=0; ii<N; ++ii){
            books2[ii+1]=books[ii];
        }

        books = books2;
        //ii=0 (dummy head)
        dp[0]=0;
        //initialize dp
        for(int ii=1; ii<=N; ++ii) dp[ii] = Integer.MAX_VALUE/2;

        //populate dp
        for(int ii=1; ii<=N; ++ii){//for each book
            int curr_thickness=0;
            int mx=0;
            for(int ss=ii; ss>=1; --ss){
                curr_thickness += books[ss][0];
                mx = Math.max(mx, books[ss][1]);
                if(curr_thickness > k) break;
                dp[ii] = Math.min(dp[ii], dp[ss-1]+mx);
            }

        }

        return dp[N];
    }
}