class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> mnq = new PriorityQueue<>(k, (a, b) -> Integer.compare(a, b));
        int N = nums.length;
        for(int ii=0; ii<N;++ii){
            if(mnq.size() < k){
                mnq.offer(nums[ii]);
            }else if(nums[ii] > mnq.peek()){
                mnq.poll();
                mnq.offer(nums[ii]);
            }
        }

        return mnq.peek();
    }
}