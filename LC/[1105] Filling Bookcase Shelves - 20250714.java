/*
 * 
 * in this exercise, we did not setupl dummy in the beginning of the array
 * in this case, we need to initialize those DPs where we might have array over bound when entering the loop
 * The mistake I made in the initial take was didn't add thickness in the loop. 
 */


class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int N = books.length;
        if(N==0) return 0;
        if(shelfWidth == 0) return 0;
        int K = shelfWidth;
        
        //declare DP
        var dp = new int[N];//no need for 2nd dimension as we do not have further constrain.
        //in 1159, the 2nd dimension was due to constrain on number of reset available
        //for each ii (book), option -> current shelf or next self.  option is constrained by shelfWidth

        //define DP
        //dp[ii]: min height @book ii (thickness, height)
        
        //initialize DP
        for(int ii=0; ii<N; ++ii) dp[ii] = Integer.MAX_VALUE/2;

        //populate DP
        //when ii=0
        dp[0]=books[0][1];
   
        for(int ii=0; ii<N; ++ii){//for each book
             int curr_mx_height=0;
             int curr_thickness = 0;
            
             for(int ss=ii; ss>=0; --ss){
                 curr_thickness += books[ss][0];
                 curr_mx_height = Math.max(curr_mx_height, books[ss][1]);
                 if(curr_thickness > K) break;

                 int prev=(ss==0)? 0:dp[ss-1]; 
                 dp[ii] = Math.min(dp[ii], prev + curr_mx_height);
             }
        }
        return dp[N-1];
    }
}

// * books[ii]: (thickness, height) - an array
// * shelfWidth: 
// * max height
// * Options: change shelf or not
// -> min_height
// * dp[ii][jj]: min hight @ book[ii] @ level jj
// dp[ii][jj] = max(dp[ii][jj], dp[ii-1][ss-1]+max(nums[ss:ii+1]))
// //Notes:
// * we need two dimensional dp here as this is type II DP. we do not know the starting point of the jj.
// * for type I DP, we only need to keep previous status (rob/no_rob). 