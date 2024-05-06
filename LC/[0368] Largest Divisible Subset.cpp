class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int N=nums.size();
        sort(nums.begin(), nums.end()); //remember to sort 
        vector<int> dp(N, 1);     //dp[ii]: considering nums[0:ii], the largest divisible subset ending @ nums[ii]
        vector<int> prev(N, -1);  //whenever DP need to output path -> record the path by prev only, do not record the whole path
        for(int ii=0; ii<N; ++ii){//Type II DP: N^2
            for(int jj=0; jj<ii; ++jj){
                if(nums[ii]%nums[jj]==0){
                    dp[ii] = max(dp[ii], dp[jj]+1);
                    if(dp[ii] == dp[jj]+1){
                        prev[ii]=jj; //record prev for trace back
                    }
                }

            }
        }

        int mxl=0;
        int idx;
        for(int ii=0; ii < N; ++ii){ //which ii is the largest
            //mxl = max(mxl, dp[ii]);
            if(dp[ii]>mxl){
                mxl = dp[ii];
                idx=ii;
            }
        }

        vector<int> ret;
        while(idx!=-1){ //trace back the largest II for path
            ret.push_back(nums[idx]);
            idx=prev[idx];
        }

        return ret;
    }
};