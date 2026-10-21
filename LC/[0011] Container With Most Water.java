class Solution {
    public int maxArea(int[] height) {
        int ll=0;
        int rr=height.length-1;
        int mx=0;
        while(ll<rr){
            int hh=Math.min(height[ll], height[rr]);
            mx=Math.max(mx, hh*(rr-ll));
            if(height[ll]<height[rr]){
                ++ll;
            }else{
                --rr;
            }
        }

        return mx;
    }
}