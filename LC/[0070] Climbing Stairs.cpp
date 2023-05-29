class Solution {
public:
    int climbStairs(int n) {
        if(n<=2) return n;
        
        int cnt=0;
        int pre=2;
        int ppre=1;
        for(int ii=3; ii<=n; ++ii){
            cnt = pre+ppre;
            ppre=pre;
            pre=cnt;
        }
        
        return cnt;
    }
};