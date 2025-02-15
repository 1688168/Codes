class Solution {
public:
    double largestSumOfAverages(vector<int>& nums, int k) {
        
        int N = nums.size();
        int sum=0;
        auto dp = vector<vector<double>>(N, vector<double>(k+1, 0));
        for(int ii=0; ii<N; ++ii){
            sum += nums[ii];
            dp[ii][1] = sum*1.0/(ii+1);
        }
        for(int kk=2; kk <= k; ++kk){//for each partition. dp is bottom up, from small to big
            for(int ii=k-1; ii< N; ++ii){ //for each ending index of last interval
                int sum=0;
                for(int jj=ii; jj>=kk-1;--jj){//starting index of last interval
                    sum+=nums[jj];
                    dp[ii][kk] = max(dp[ii][kk], dp[jj-1][kk-1]+sum*1.0/(ii-jj+1));
                }

            }
        }