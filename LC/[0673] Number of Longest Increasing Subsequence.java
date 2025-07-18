class Solution {
    public int findNumberOfLIS(int[] nums) {
        int N = nums.length;
        
        var dp = new int[N];
        var cnt = new int[N];

        //dp[ii]: LIS @ ii
        //cnt[ii]: count of LIS @ ii

        //initialize dp
        for(int ii=0; ii<N; ++ii){
            dp[ii]=1;
            cnt[ii]=1;
        }

        //when ii=0
        
        //populate DP
        for(int ii=1; ii<N; ++ii){//for each ii
            for(int jj=0; jj<ii; ++jj){//for each jj before ii
                if(nums[jj]>= nums[ii]) continue;//ignore those that is not strictly increasing
                    if(1+dp[jj]>dp[ii]){//a new  LIS
                        dp[ii] = Math.max(dp[ii], 1+dp[jj]);
                        cnt[ii]=cnt[jj];
                    }else if (1+dp[jj]==dp[ii]){//LIS @ jj can also contribute cnt for LIS @ ii
                        cnt[ii]+=cnt[jj];
                    }
            }
        }
        

        //traverse ii to find LIS and return cnt[ii]
        int ans=-1;
        int mx=-1;
        for(int ii=0; ii<N; ++ii){
            if(dp[ii] > mx){//new LIS
                mx=dp[ii];
                ans=cnt[ii];
            }else if(dp[ii]==mx){//multiple LIS at diff ii
                ans += cnt[ii];
            }
        }
        return ans;
        
    }
}

// * N=2000 -> N^2
// * count num of LIS -> whenver we find a LIS, we need to record the count
// * how to find LIS? -> DP (current problem (status), can be derived from sub-problem (prev-status))