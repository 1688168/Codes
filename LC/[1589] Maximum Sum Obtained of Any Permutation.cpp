class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        int N = nums.size();
        vector<int> events(N+1, 0);

        for(auto request: requests){
            events[request[0]] += 1;
            events[request[1]+1] -=1;
        }

        vector<int> freq(N);
        int pre = 0;
        for(int ii=0; ii<N; ++ii){
            pre = pre + events[ii];
            freq[ii] = pre;
        }

        sort(freq.begin(), freq.end());
        sort(nums.begin(), nums.end());

        long ret = 0;
        long M = 1e9+7;
        for(int ii=0; ii<N; ++ii){
            ret = (ret + (long)freq[ii]*(long)nums[ii]) %M;
        }
        return ret;
    }
};