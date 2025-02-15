class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        int N = nums.size(); //take size
        nums.insert(nums.begin(), 0);//insert dummy 
        auto dp = vector<vector<double>>(N+1, vector<double>(k+1, INT_MIN));

        //for(int ii=0; ii<=N; ++ii)dp[ii][0]=INT_MIN;
        dp[0][0]=0;
        for(int ii=1; ii<=N; ++ii){//for each element (we have dummy header)
            //let kk start from 2 and initialize kk=1 can be another way doing this
            for(int kk=1; kk<=min(k, ii); ++kk){//for each num of partition
                //for(int jj=k; jj<=ii; ++jj){//try each starting index of last partition
                double sum=0;
                for(int jj=ii; jj>=kk; --jj){//jj is the starting index of last subarray
                    sum+=nums[jj];
                    dp[ii][kk] = max(dp[ii][kk], dp[jj-1][kk-1]+sum/(ii-jj+1));//[0:jj] with kk-1 partitions and [jj:N+1] with one partition
                }
            }
        }
        double ans=0;
        for(int kk=1; kk<=k; ++kk){
            ans = max(ans, dp[N][kk]);
        }
        return ans;
    }
};