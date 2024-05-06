class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        //when do you need to insert a dummy head?
        //when ii has something to do with ii-1
        books.insert(books.begin(), {0,0});
        int N = books.size();
        vector<int> dp(N, INT_MAX);
        dp[0]=0; //always need to initialize DP

        /* DP Type II - Basic */
        for(int ii=1; ii<N; ++ii){          //DP type II - Basic 
            int max_height=0;
            int total_width=0;
            for(int jj=ii; jj >=1; --jj){ //try all possibility that can be on this shelf ending with books[ii]
                max_height=max(max_height, books[jj][1]);
                total_width += books[jj][0];
                if(total_width > shelfWidth) break;
                dp[ii]=min(dp[ii], dp[jj-1]+max_height);
            }
        }
        return dp[N-1];
    }
};
/*
dp[ii] = min height of bookshelf @ iith book
dp[ii]=dp[jj]+max(height @ current shelf)
*/