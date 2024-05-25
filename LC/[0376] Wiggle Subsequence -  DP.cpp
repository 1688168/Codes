class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()==0) return 0;
        
        /*
        let p be max wiggle len ending @ down-slope
            q be max wiggle len ending @ up-slope
        */
        int p=1, q=1;
        for(int ii=1; ii<nums.size(); ++ii){
            if(nums[ii] > nums[ii-1]){//current is uplope
                q=p+1;//upslope can increment down-slope
            }else if(nums[ii] < nums[ii-1]){//current is down-slope
                p=q+1;//down-slope can only increment upslope
            }
        }

        return max(p, q);
    }
};