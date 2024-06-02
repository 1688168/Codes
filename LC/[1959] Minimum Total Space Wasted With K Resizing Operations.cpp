class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        int n = nums.size();//all elements need to fit in the dynmic array
        /*
        dp[ii][jj]: min space wasted on iith element, with jj resizing
                          sz
        x x x x x [x x ii]

        for s in [0, ii+1]:
            dp[ii][jj] = min(dp[ii][jj], dp[s-1][jj-1] + WasteSpace(S:ii+1))
            where WasteSpace(s:ii+1) = max[s:ii+1]*(ii-s+1) - intervalSum[s:ii+1]
        */
        int dp[n][k+1];//declare the dp with size of input array, k+1 resizing capacity

        //initialize the array to max (we are looking for min wasted space)
        for(int ii=0; ii<n; ++ii){
            for(int jj=0; jj<=k; ++jj){
                dp[ii][jj]=INT_MAX/2;
            }
        }

        int mx=0;
        int sum=0;
        for(int ii=0; ii<n; ++ii){//initialize when jj=0. (there is no jj-1)
            mx = max(mx, nums[ii]);
            sum+=nums[ii];
            dp[ii][0]=mx*(ii+1)-sum;
        }

        for(int ii=1; ii<n; ++ii){//for each element.  check where could idx out of range
            for(int jj=1; jj<=min(ii, k); ++jj){//try all the resizing
              
                int mx=0;
                int intervalSum=0;
                //update dp[ii][jj]
                for(int ss=ii; ss>=1; --ss){//for each ii as the ending element, try all to be in this resizing and capture the min
                    mx=max(mx, nums[ss]);
                    intervalSum += nums[ss];
                    dp[ii][jj] = min(dp[ii][jj], dp[ss-1][jj-1]+mx*(ii-ss+1) - intervalSum);
                }
            }
        }

        int ans = INT_MAX/2;
        for(int jj=0; jj<=k; ++jj){
            ans = min(ans, dp[n-1][jj]);
        }
        return ans;
    }
};