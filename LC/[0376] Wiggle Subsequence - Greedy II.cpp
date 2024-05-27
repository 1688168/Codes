class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int ret=1;
        int dir=-2; //special assignment for initial slope

        if (nums.size()==0) return 0;
        for(int ii=1; ii < nums.size(); ++ii){
            int dir_prev = dir;
            if(nums[ii] > nums[ii-1])//find out current slope
                dir=1;
            else if (nums[ii] < nums[ii-1])
                dir=-1;
            else //inheriting prev non-zero slope
                dir=dir_prev;
            
            if(dir != dir_prev)
                ret += 1;
        }
        return ret;
    }
};