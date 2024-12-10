class Solution {
    int dp[1005][1005];
public:
    int maximumProcessableQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        dp[0][n-1] = 0;//initially, we performed zero query
        for(int len=n; len>=1; --len){//from big interval and reducing
            for(int ii=0; ii+len-1<n; ++ii){//ii as starting interval
                int jj=ii+len-1; //jj as the ending of the interval
                if(ii-1>=0){//current interval is from previous bigger interval. remember, we are going from bigger to smaller
                    int kk=dp[ii-1][jj];//how many queries we have done in previous bigger interval?
                    if(kk < queries.size() && nums[ii-1] >= queries[kk]){
                        dp[ii][jj] = max(dp[ii][jj], dp[ii-1][jj]+1);
                    }else{
                        dp[ii][jj] = max(dp[ii][jj], dp[ii-1][jj]);
                    }
                }
                if(jj+1<n){
                    int kk=dp[ii][jj+1];
                    if(kk < queries.size() && nums[jj+1] >= queries[kk])
                        dp[ii][jj] = max(dp[ii][jj], dp[ii][jj+1]+1);
                    else
                         dp[ii][jj] = max(dp[ii][jj], dp[ii][jj+1]);
                }
            }
        }
        int ret = 0;
        for(int ii=0; ii<n; ++ii){
            int kk=dp[ii][ii];//single char left, can we still remove it? (above len min was 1. but can we remove last char?)
            if(kk < queries.size() && nums[ii] >=queries[kk])
                ret = max(ret, dp[ii][ii]+1);
            else
                ret = max(ret, dp[ii][ii]);
            
        }
        return ret;
    }
};