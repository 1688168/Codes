class Solution {
    public:
    int lastStoneWeightII(vector<int> A) {
        bitset<1501> dp = {1};
        int sumA = 0;
        for (int a : A) {//for each stone
            sumA += a;//for pruning
            for (int i = min(1500, sumA); i >= a; --i)
                dp[i] = dp[i] + dp[i - a];//bit addition. this is like OR
        }
        for (int i = sumA / 2; i >= 0; --i)
            if (dp[i]) return sumA - i - i; //sum(B)-sum(A)=Total-2*sum(A) << B is guaranteed bigger
        return 0;
    }
};