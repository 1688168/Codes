class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        auto len = vector<int>(n, 1);//[c++][vector][initialize vector size and value]
        auto times = vector<int>(n, 1);

        for(int ii=0; ii<n; ++ii){
            for(int jj=0; jj<ii; ++jj){
                if(nums[jj]>=nums[ii]) continue;
                if(len[jj]+1 > len[ii]){
                    len[ii] = max(len[ii], len[jj]+1);
                    times[ii]=times[jj];
                }else if(len[jj]+1 == len[ii]){
                    times[ii] += times[jj];
                }
            }
        }
        int maxLen = 0;
        int result;
        for(int ii=0; ii<n; ++ii){
            if(len[ii] > maxLen){
                maxLen=len[ii];
                result=times[ii];
            }else if(len[ii]==maxLen){
                result += times[ii];
            }
        }
        return result;
    }
};