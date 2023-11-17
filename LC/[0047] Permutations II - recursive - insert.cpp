class Solution {
public:
    vector<vector<int>> results;
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        vector<int>perm;
        DFS(perm,0,nums);
        return results;
    }
    /*
    1. k is the index of nums to be inserted 
    */
    void DFS(vector<int>perm, int k, vector<int>& nums)
    {
        if (k==nums.size()) //when index of num is N, we are done
        {
            results.push_back(perm);
            return;
        }
        
        for (int i=0; i<k+1; i++) //when we are inserting k=0 (empty), we have 0+1 position to insert
        {
            vector<int>newPerm = perm;
            if (i==0 || i>=1 && nums[k]!=perm[i-1]) //if nums[k] is same as index of pre-num, bail
            {
                newPerm.insert(newPerm.begin()+i, nums[k]);
                DFS(newPerm, k+1, nums);
            }
            else
                return;            
        }
            
    }
};