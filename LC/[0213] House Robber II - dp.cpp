class Solution {
    public:
        int rob(vector<int>& nums) {
            int n = nums.size();
            int rob, norob, rob_tmp;
            int ret=0;
    
            //first (0) norob
            rob = 0;
            norob=0;
    
            for(int ii=1; ii<n; ++ii){
                int rob_tmp = rob, norob_tmp = norob;//DPI O(1) space solution always need tmp to avoid conflicts
                rob = norob_tmp + nums[ii]; //the max profit @ ii and rob ii
                norob= max(rob_tmp, norob_tmp);//the max profit @ ii and not rob ii
            }
            ret = max(rob, norob);
    
            //first (0) rob
            rob = nums[0];
            norob=0;
            for(int ii=1; ii<n-1; ++ii){
                int rob_tmp = rob, norob_tmp = norob;//DPI O(1) space solution always need tmp to avoid conflicts
                rob = norob_tmp + nums[ii]; //the max profit @ ii and rob ii
                norob= max(rob_tmp, norob_tmp);//the max profit @ ii and not rob ii
            }
            ret = max(ret, max(rob, norob));
    
            return ret;
        }
    };