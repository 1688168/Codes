class Solution {
    public int tribonacci(int n) {
        if(n<=1) return n;
        if(n==2) return 1;

        int prev=1;
        int prevprev=1;
        int prevprevprev=0;
        int curr=0;
        for(int ii = 3; ii<=n; ++ii){
            curr = prev+prevprev+prevprevprev;
            prevprevprev=prevprev;
            prevprev=prev;
            prev=curr;
        }
        return curr;
    }
}