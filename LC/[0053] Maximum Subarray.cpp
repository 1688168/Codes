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
