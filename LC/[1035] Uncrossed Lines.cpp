class Solution {
    public:
        int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
            //this is same as LCS: longest common subsequence
            int N1 = nums1.size();
            int N2 = nums2.size();
    
            nums1.insert(nums1.begin(), 0);
            nums2.insert(nums2.begin(), 0);
    
            auto dp = vector<vector<int>>(N1+1, vector<int>(N2+1, 0));
            for(int ii=1; ii<=N1; ++ii){
                for(int jj=1; jj<=N2; ++jj){
                    if(nums1[ii]==nums2[jj]){
                        dp[ii][jj] = dp[ii-1][jj-1]+1;
                    }else{
                        dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1]);
                    }
                }
            }
    
    
            return dp[N1][N2];
        }
    };
    
    /*
    * two series
    * nums1:
    * nums2:
    */