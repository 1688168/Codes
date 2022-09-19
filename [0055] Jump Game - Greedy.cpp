class Solution {
public:
    bool canJump(vector<int>& nums) {

        int far = 0;
        for(int i = 0; i<nums.size()-1; i++) //simulating moving idx by idx
        {
            if (far < i) return false;//we cannot move beyound the farest we could
            far = max(far,i+nums[i]);
        }

        return far>=nums.size()-1;
    }
};
