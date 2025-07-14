class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int N = books.length;

        
    }
}

* books[ii]: (thickness, height) - an array
* shelfWidth: 
* max height
* Options: change shelf or not
-> min_height
* dp[ii][jj]: min hight @ book[ii] @ level jj
dp[ii][jj] = max(dp[ii][jj], dp[ii-1][ss-1]+max(nums[ss:ii+1]))
//Notes:
* we need two dimensional dp here as this is type II DP. we do not know the starting point of the jj.
* for type I DP, we only need to keep previous status (rob/no_rob). 