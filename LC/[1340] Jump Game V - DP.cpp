class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int N = arr.size();

        //declare and initialize the DP
        vector<int>dp(N, 1);

        //sort the array        
        vector<pair< int, int>>p;
        for(int ii=0; ii<N; ++ii){
            p.push_back({arr[ii], ii});
        }

        sort(p.begin(), p.end());//sort by height ascending
        reverse(p.begin(), p.end());//sorted by height decending

        for(int ii=0; ii<N; ++ii){
            int idx = p[ii].second;
            for(int jj=idx+1; jj<=min(N-1, idx+d); ++jj){
                if(arr[jj] >= arr[idx]) break; //cannot have anything higher in between
                dp[jj] = max(dp[jj], dp[idx]+1);
            }

            for(int jj=idx-1; jj>=max(0, idx-d); --jj){
                if(arr[jj] >= arr[idx]) break; //cannot have anything higher in between
                dp[jj] = max(dp[jj], dp[idx]+1);
            }
        }

        int ret = 0;
        for(int ii=0; ii<N; ++ii){
            ret = max(ret, dp[ii]);
        }
        return ret;
    }
};