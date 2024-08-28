/*
1 <= rods[i] <= 1000: this hints that DP is the range of the value, not the index of the elements
2. equal -> diff=0
*/

class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        int offset = 5000;
        vector<int>dp(2*offset+1, -1);//default to -1 indicating cannot make the diff
        dp[0+offset]=0;
        int N = rods.size();
        for(int ii=0; ii<N; ++ii){ //for each item [0, N-1]
            int ll = rods[ii];
            auto dp_old = dp;
            for(int diff=-offset; diff<=offset; ++diff){
                if(dp_old[diff+offset]==-1) continue;
                if(diff+ll < offset)
                    dp[diff+ll+offset] = max(dp[diff+ll+offset], dp_old[diff+offset]+ll);
                if(diff-ll >= -offset)
                    dp[diff-ll+offset] = max(dp[diff-ll+offset], dp_old[diff+offset]);
            }
        }
        return dp[0+offset];
    }
};

/*
dp[left][right]

for(int ii=0; ii<N; ++ii){
    int l = rod[ii];

    for(int left=0; left <= 2500; ++left){
        for(int right=0; right<=2500; ++right){
            if(dp[left][right]==true){
                dp[left+l][right]=true;
                dp[left][right+l]=true;

                if(left+l==right) result => left+l;
                if(right+l==left) result => right+l;
            }
        }
    }
}


dp[diff] //the maximum left when left-right==diff

for(int ii=0; ii<N; ++ii){
    int l = rod[ii];
    for(int diff=-500; diff <=5000; ++diff){
        dp[diff+l] = dp_old[diff]+l
        dp[diff-l] = dp_old[diff]
    }
}

return dp[0];
*/