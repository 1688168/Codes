/********************
 * 20240512
***********************/
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        /*
         + nums[ii]: (distinct) postive int
         -> largest subset
         s.t.: all pairs divisible
         * when we are finding subset->sort

        # idea: 
        * all pairs divisible a/b where a>b
        * if we sort answer
        * answer[ii] divisible answer[ii-1] then answer[ii] can be divisible by all answer[jj]  

        # we are looking for jj < ii and nums[ii]%nums[jj]==0 -> type II DP
        */
        nums.insert(nums.begin(), 0); //insert a dummy header
        int N = nums.size();
        sort(nums.begin(), nums.end());
        vector<int> dp(N,  1);
        vector<int> prev(N,  -1);
        vector<int> answer;
        
        //initialize dp
        dp[0]=0;

        //we need to output path. -> record prev
        /*
            dp[ii] is the largest divisible subset ending at ii
            dp[ii] = max(dp[ii], dp[jj] + 1) where jj < ii and nums[ii]%nums[jj]==0
            prev[ii]=jj
        */

        //find out dp and identify the size of largest divisible subset
        for(int ii=1; ii<N; ++ii){
            for(int jj=ii-1; jj>=1; --jj){
                if(nums[ii]%nums[jj]!=0) continue;//skip those not divisible
                if(dp[jj]+1 > dp[ii]){
                    prev[ii]=jj;
                    dp[ii]=dp[jj]+1;
                }
            }
        }
        //traverse the dp[ii], once found the max_size, trace back for the path
        int mx_sz = *(std::max_element(dp.begin(), dp.end()));

        // cout << " dp: " << endl;
        // for(int ii=0; ii<N; ++ii){
        //     cout << dp[ii] << "->";
        // }
        // cout << endl;
        // cout << " prev: " << endl;
        // for(int ii=0; ii<N; ++ii){
        //     cout << prev[ii] << "->";
        // }
        // cout << endl;
        // cout << " mx_sz: " << mx_sz << endl;
        for(int ii=1; ii<dp.size(); ++ii){ //locate one max size idx
            if(dp[ii]==mx_sz){
                int jj = ii;
                while(jj>=0){
                    answer.push_back(nums[jj]);
                    jj=prev[jj];
                }
                break;
            }
        }

        return answer;
    }
};


/*---------------------------------------------------- */
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int N=nums.size();
        sort(nums.begin(), nums.end()); //remember to sort 
        vector<int> dp(N, 1);     //dp[ii]: considering nums[0:ii], the largest divisible subset ending @ nums[ii]
        vector<int> prev(N, -1);  //whenever DP need to output path -> record the path by prev only, do not record the whole path
        for(int ii=0; ii<N; ++ii){//Type II DP: N^2
            for(int jj=0; jj<ii; ++jj){
                if(nums[ii]%nums[jj]==0){
                    dp[ii] = max(dp[ii], dp[jj]+1);
                    if(dp[ii] == dp[jj]+1){
                        prev[ii]=jj; //record prev for trace back
                    }
                }

            }
        }

        int mxl=0;
        int idx;
        for(int ii=0; ii < N; ++ii){ //which ii is the largest
            //mxl = max(mxl, dp[ii]);
            if(dp[ii]>mxl){
                mxl = dp[ii];
                idx=ii;
            }
        }

        vector<int> ret;
        while(idx!=-1){ //trace back the largest II for path
            ret.push_back(nums[idx]);
            idx=prev[idx];
        }

        return ret;
    }
};