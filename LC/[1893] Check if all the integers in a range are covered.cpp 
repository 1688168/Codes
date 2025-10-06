class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        vector<int> diff(100 , 0);
        for(auto range: ranges){
            diff[range[0]] += 1;
            diff[range[1]+1] -= 1;
        }

        int sum = 0;
        for(int ii=1; ii<=50; ++ii){
            sum += diff[ii];
            if(ii>=left && ii<=right && sum == 0) return false;
        }
        return true;
    }
};