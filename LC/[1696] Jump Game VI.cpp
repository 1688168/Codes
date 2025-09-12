class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int N = nums.size();
        deque<pair<int, int>> dq;
        dq.push_back({nums[0], 0});
        for(int ii=1; ii<N; ++ii){
            if(!dq.empty() && ii-dq.front().second > k) dq.pop_front();
            int currSteps = dq.front().first + nums[ii];
            while(!dq.empty() && currSteps > dq.back().first) dq.pop_back();
            dq.push_back({currSteps, ii});
        }

        return dq.back().first;
        
    }
};