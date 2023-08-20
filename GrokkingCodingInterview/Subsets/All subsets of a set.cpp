void helper(vector<vector<int>> & res, int sz, int st, vector<int> & path, vector<int> & nums){
    if(sz==0){
        res.push_back(path);
        return;
    }
    if(sz<0) return;

    for(int ii=st; ii< nums.size(); ++ii){
        path.push_back(nums[ii]);
        helper(res, sz-1, ii+1, path, nums);
        path.pop_back();
    }

    return;
}

vector<vector<int>> FindAllSubsets(vector<int> nums)
{
    int N=nums.size();

    vector<vector<int>> res;
    vector<int> path;
    for(int sz=0; sz<=N; ++sz) helper(res, sz, 0, path, nums);
    

    return res;
}