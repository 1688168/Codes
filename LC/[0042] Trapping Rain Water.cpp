class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> leftMost(n, 0); //leftMost[ii]: the highest bar to the left of i
        vector<int> rightMost(n, 0);
        for(int ii=1; ii< n; ++ii){
            leftMost[ii] = max(leftMost[ii-1], height[ii-1]);
        }
        for(int ii=n-2; ii>=0; --ii){
            rightMost[ii] = max(rightMost[ii+1], height[ii+1]);
        }

        int ret = 0;
        for(int ii=0; ii<n; ++ii){
            int h = min(leftMost[ii], rightMost[ii]) -height[ii];
            ret += max(0,h);
        }

        return ret;
    }
};