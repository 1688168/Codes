class Solution {
    private Boolean isFeasible(int[] nums, int mm, int kk){
        int N = nums.length;
        int cnt=0;

        //can you do this by stream?
        int ii=0;
        while(ii<N){
            int sum=0;
            int jj=ii;
            while(jj < N && nums[jj]+sum <= mm){
                sum+=nums[jj];
                ++jj;
            }
            ++cnt;
            ii=jj;                   
        }

        return cnt <= kk;
    }
    public int splitArray(int[] nums, int k) {
        int ans=0;
        int N = nums.length;

        // java use stream find min/max value in an array
        int ll =  Arrays.stream(nums).max().getAsInt();//java find min/max in an array
        int rr = Integer.MAX_VALUE;//java max int
        //System.out.println("ll: " + ll);
        while(ll <= rr){//binary search pattern (by value)
            int mm=ll+(rr-ll)/2;
            if(isFeasible(nums, mm, k)){
                ans=mm;
                rr=mm-1;
            }else{
                ll=mm+1;
            }
        }

        return ans;
    }
}