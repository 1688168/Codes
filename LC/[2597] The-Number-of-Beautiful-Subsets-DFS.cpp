class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) 
    {
        return dfs(0, 0, nums, k) - 1;
    }

    int dfs(int cur, int state, vector<int>& nums, int k)
    {
        if (cur==nums.size()) return 1;

        int has_prior_diff_k = 0;
        for (int i=0; i<cur; i++)
        {
            if ((state>>i)&1 && abs(nums[i]-nums[cur])==k)
            {
                has_prior_diff_k = 1;
                break;
            }
        }

        if (has_prior_diff_k == 1){
            return dfs(cur+1, state, nums, k);
        }else{
            return dfs(cur+1, state, nums, k) + dfs(cur+1, state+(1<<cur), nums, k);
        }
    }
};