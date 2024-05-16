/*
space O(N):
*/
class Solution {
    /* Kadane's algorithm for max subarray sum 
       dp[ii]: max subarray sum ending @ ii
       dp[ii] = max(nums[ii], dp[ii-1]+nums[ii] if nums[ii]> nums[ii-1] else 0)
    */
public:
    int maxSubArray(vector<int>& nums) {
       
        nums.insert(nums.begin(), 0);
        int N=nums.size();
        vector<int> dp(N, 0);

        int mxs=INT_MIN;
        for(int ii=1; ii<N; ++ii){
           
            dp[ii]= nums[ii] + (dp[ii-1] > 0? dp[ii-1]:0);
            mxs=max(mxs, dp[ii]);
        }
        return mxs;
        
    }
};


//O(1) space
//O(1) space
#include <bits/stdc++.h>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp=INT_MIN;

        int mxs=INT_MIN;
        dp=nums[0];
        mxs=dp;
        for(int ii=1; ii<nums.size(); ++ii){
            dp=max(dp+nums[ii], nums[ii]);
            mxs=max(mxs, dp);
        }
        return mxs;
    }
};

//O(N) solution
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> v(nums.size(), 0);

        v[0]=nums[0];
        int mm = v[0];
        for(int ii=1; ii < nums.size(); ++ii){
            v[ii] = nums[ii] + (v[ii-1]>0? v[ii-1]:0);
            mm=max(mm, v[ii]);
        }

        return mm;
    }
};
