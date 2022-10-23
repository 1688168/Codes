class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> visited;
        for(auto n: nums){
            if(visited.find(n) != visited.end()){
                return true;
            }
            visited.insert(n);
        }
        return false;
    }
};
