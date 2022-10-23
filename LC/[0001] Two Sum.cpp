class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> val2idx;

        for(int ii=0; ii<nums.size(); ++ii){
            auto curr=nums[ii];
            if(val2idx.find(target-curr) != val2idx.end()){
                return {ii, val2idx[target-curr]};
            }
            val2idx[curr]=ii;
        }
        return {};
    }
};
