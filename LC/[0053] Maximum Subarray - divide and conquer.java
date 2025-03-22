class Solution {
    private int helper(int[] nums, int st, int ed){
        /* max subarray sum is the max of 
        * 1. max subarray sum from left
        * 2. max subarray sum from right
        * 3. max subarray sum from center 
        */

        //base case, only one element. max non-null subarray sum is itself
        if(st==ed) return nums[st];

        //divice: partition nums from center
        int mm = st+(ed-st)/2;

        //max subarray sum from center going left
        int max_mm_left = Integer.MIN_VALUE, acc = 0;
        for (int ii = mm; ii >= st; --ii) {
            max_mm_left = Math.max(max_mm_left, acc += nums[ii]);
        }

        //max subarray sum from center going right
        int max_mm_right = Integer.MIN_VALUE;
        acc=0;
        for(int ii=mm+1; ii<=ed; ++ii){
            max_mm_right = Math.max(acc += nums[ii], max_mm_right);
        }


        //max subarray sum from left
        int leftMax=helper(nums, st, mm);

        //max subarray sum from right
        int rightMax=helper(nums, mm+1, ed);
        
        //[java:] find max out of int array.  [java:] how to find max from more than 2 elements, [java:] max
        return IntStream.of(max_mm_left+max_mm_right, leftMax, rightMax)
                        .max()
                        .orElse(Integer.MIN_VALUE);
    }
    public int maxSubArray(int[] nums) {
        //max subarray sum 
        return helper(nums, 0, nums.length-1);
    }
}