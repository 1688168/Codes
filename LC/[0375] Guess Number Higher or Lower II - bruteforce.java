/*
Problem statement:
* given n: [1, n]
* guess x, if correct before use up all money win, otherwise, pay x
* min amount of money you need to have in order to win given n

Analysis:

o o o o x o o o n

required_money = x + max([1, x-1], [x+1], n)
-> recursion on interval
-> dp on interval: bigger interval is derived from previous smaller intervals


*/
class Solution {
    //private Map<Integer, Integer> mm = new HashMap<>();

    private int getMoney(int st, int ed){
        if(st >= ed) return 0;
        int ans=Integer.MAX_VALUE;//java max int
        for(int xx=st; xx<=ed; ++xx)
            ans = Math.min(ans, xx + Math.max(getMoney(st, xx-1), getMoney(xx+1, ed)));
        return ans;
    }
    public int getMoneyAmount(int n) {
        return getMoney(1, n);    
    }
}