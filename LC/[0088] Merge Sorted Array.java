class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int ii=m-1, jj=n-1, N=m+n;
        int kk=N-1;

        while(ii >=0 && jj >= 0){
            if(nums1[ii] >= nums2[jj]){
                nums1[kk--]=nums1[ii--];
                
            }else{
                nums1[kk--]=nums2[jj--];
            }
        }
        
        while(jj>=0){
            nums1[kk--]=nums2[jj--];
        }

    }
}