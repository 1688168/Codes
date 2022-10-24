class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        int ans=0;
        sort(begin(nums), end(nums));

        int N=nums.size();
        for(int ii=0; ii<N-2; ++ii){
            ans += two_sum_less(ii+1, target-nums[ii], nums);
        }

        return ans;

    }

    int two_sum_less(int idx, int target, vector<int> & nums){
        int ttl=0;
        for(int ii=idx; ii<nums.size()-1; ++ii){
            int ll=ii+1, rr=nums.size()-1, ans=-1;
            int ntg=target-nums[ii];
            if(nums[ll] >= ntg)break;
            while(ll<=rr){
                int mm=ll+(rr-ll)/2;
                if(nums[mm] < ntg){
                    ans=mm;
                    ll=mm+1;
                }else{
                    rr=mm-1;
                }
            }

            if(ans != -1){
                ttl += (ans-ii);
            }
        }
        return ttl;
    }
};
