class Solution {
public:

    int mem[1001];//default to all zero

    int maxJumps(vector<int>& arr, int d) {
        int ret = 0;
        for(int ii=0; ii<arr.size(); ++ii){//try each starting point
            dfs(ii, arr, d);
            ret = max(ret, mem[ii]);
        }
        return ret;
    }

    int dfs(int idx, vector<int> & arr, int D){
        //visited?
        if(mem[idx] != 0) return mem[idx];

        //going right
        int ret = 1;
        for(int kk=1; kk<=D; ++kk){ //for each kk between (jj, ii)
            if(idx+kk >= arr.size()) break;//no need to try further
            if(arr[idx+kk] >= arr[idx]) break;
            ret = max(dfs(idx+kk, arr, D)+1, ret);
        }

        //going left
        for(int kk=1; kk<=D; ++kk){ //for each kk between (jj, ii)
            if(idx-kk < 0) break;//no need to try further
            if(arr[idx-kk] >= arr[idx]) break;
            ret = max(dfs(idx-kk, arr, D)+1, ret);
        }

        mem[idx] = ret;
        return ret;
    }
};