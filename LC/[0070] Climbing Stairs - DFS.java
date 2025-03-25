class Solution {

    public int climbStairs(int n) {
        if(n <= 2) return n;
        return climbStairs(n-2) + climbStairs(n-1);
        
    }
}