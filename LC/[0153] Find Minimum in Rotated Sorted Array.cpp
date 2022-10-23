class Solution {
public:
    int findMin(vector<int>& nums) {
        int ll=0;
        int rr=nums.size()-1;
        int ans=-1;
        int N=nums.size();
        if(nums[0] <= nums[N-1]) return nums[0];

        while(ll<=rr){
            int mm=ll+(rr-ll)/2;
            if(nums[mm] > nums[N-1]){ //on the left, need to search right.  left cannot have answer
                ll=mm+1;
            }else{
                ans=nums[mm]; //hold the potential answer
                rr=mm-1;
            }
        }
        return ans;
    }
};
