class Solution {
    private boolean moreK(int mm, int[] nums, int k){
        int cnt=0;
        for(var nn: nums){
            if(nn>=mm){
                ++cnt;
                if(cnt>=k) return true;
            }
        }
        
        return false;
    }
    public int findKthLargest(int[] nums, int k) {
        int N=nums.length;

        // int ll = Arrays.stream(nums).min();
        // int rr = Arrays.stream(nums).max();

        int ll = Arrays.stream(nums).min().getAsInt();
        int rr = Arrays.stream(nums).max().getAsInt();

        int ans=-1;
        while(ll<=rr){
            int mm = ll+(rr-ll)/2;
            if(moreK(mm, nums, k)){
                ans=mm;
                ll=mm+1;
            }else{
                rr=mm-=1;
            }
        }
        return ans;
    }
}