class Solution {
public:

    int kadane(vector<int> & arr){
        //try kadane's Algorithm
        vector<int> dp1(arr.size(), 0);
        int dp2=0;

        int lmv=0;
        int curr_sum=0;
        for(int ii=0; ii<arr.size(); ++ii){
            curr_sum=max(curr_sum+arr[ii], arr[ii]);
            dp1[ii]=curr_sum;
        }
        dp2=0;
        for(int ii=arr.size()-1; ii>=0; --ii){
            dp2=max(dp2+arr[ii], arr[ii]);

            if(arr[ii]==-1){
                lmv=max(lmv, dp1[ii]+dp2-arr[ii]);
            }
        }

        return lmv;


    }
    int largestVariance(string s) {
        //count all char occurance
        vector<int> counts(26, 0);
        int ans=0;
        for(auto c: s){
            ++counts[c-'a'];
        }

        // for(auto x: counts){
        //     cout << x << ",";
        // }
        // cout << endl;
        for(int ii=0; ii<26; ++ii){
            for(int jj=0; jj<26; ++jj){
                if(ii==jj) continue;
                if(counts[ii]==0 || counts[jj]==0) continue;
                //construct the converted 1,0 string
                vector<int> arr(s.size(), 0);
                for(int kk=0; kk<s.size(); ++kk){
                    if(s[kk]-'a'==ii)
                        arr[kk]=1;
                    else if(s[kk]-'a'==jj)
                        arr[kk]=-1;

                }
                auto var=kadane(arr);
                ans=max(var, ans);

            }
        }

        return ans;

    }
};
