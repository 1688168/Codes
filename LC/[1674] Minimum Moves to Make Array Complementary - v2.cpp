class Solution {
    map<int, int> diff;//sorted hash (we need the order)
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        for(int ii=0; ii<n/2; ++ii){
            int a = min(nums[ii], nums[n-1-ii]);
            int b = max(nums[ii], nums[n-1-ii]);
            diff[2] += 2;
            diff[a+1] -= 1;
            diff[a+b] -= 1;
            diff[a+b+1] += 1;
            diff[limit+b+1] += 1;
        }

        int y = 0;
        int ret = INT_MAX;
        for(auto kv: diff){
            y += kv.second;
            ret = min(ret, y);
        }
        return ret;
    }
};