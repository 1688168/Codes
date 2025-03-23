class Solution {
    public int fib(int n) {
        if(n<2) return n;
        int prev=1, prevprev=0;
        int res=0;
        for(int ii = 2; ii<=n; ++ii){
            res = prev + prevprev;
            prevprev=prev;
            prev=res;
        }

        return res;
    }
}