class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int ll = *std::max_element(nums.begin(), nums.end());
        int rr = INT_MAX;
        while(ll<rr){
            int mm = ll+(rr-ll)/2;
            if(isFeasible(nums, k, mm)){
                rr = mm;
            }else{
                ll= mm+1;
            }

        }
        return ll;
        
    }

    bool isFeasible(vector<int> & nums, int kk, int mm){
        int count=0;
        for(int ii=0; ii<nums.size(); ++ii){
            int jj=ii;
            int sum=0;
            while(jj<nums.size() && sum+nums[jj] <= mm){
                sum += nums[jj];
                ++jj;
            }
            ++count;
            ii = jj-1;
        }

        return count <= kk;
    }
};