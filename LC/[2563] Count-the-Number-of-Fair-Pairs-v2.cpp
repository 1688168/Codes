class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) 
    {
        sort(nums.begin(), nums.end());
        
        long long ret = 0;
        for (int ii=1; ii< nums.size(); ++ii)
        {
            auto x=nums[ii];
            int k = upper_bound(nums.begin(), nums.begin()+ii+1, upper-x) - nums.begin();
            int t = lower_bound(nums.begin(), nums.begin()+ii+1, lower-x) - nums.begin();
            int count = k-t;
            
            if (x+x<=upper && x+x>=lower)
                count--;
            
            ret += count;            
        }
        
        return ret;
        
    }
};