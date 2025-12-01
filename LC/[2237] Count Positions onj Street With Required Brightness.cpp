class Solution {
public:
    int meetRequirement(int n, vector<vector<int>>& lights, vector<int>& requirement) {
        vector<int> diff(n+1);
        for(int ii=0; ii<lights.size(); ++ii){
            int a = max(0, lights[ii][0] - lights[ii][1]);
            int b = min(n-1, lights[ii][0] + lights[ii][1]);
            diff[a] += 1;
            diff[b+1] -= 1;
        }

        int sum=0;
        int ret=0;
        for(int ii=0; ii<n; ++ii){
            sum += diff[ii];
            if(sum >= requirement[ii]) ret++;
        }

        return ret;

    }
};