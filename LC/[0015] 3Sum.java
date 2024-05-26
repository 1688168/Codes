class Solution {
    public List<List<Integer>> two_sum(int st, int target, int[] nums){
        List<List<Integer>> res = new ArrayList<>();//how to declare ArrayList

        int ll=st, rr=nums.length-1; //array length is an attribute
        while(ll<rr){
            int a=nums[ll], b=nums[rr];

            if(a+b==target){
                res.add(Arrays.asList(a, b));//how to construct array from int
                ++ll;
                --rr;
                while(ll<rr && nums[ll]==nums[ll-1])++ll;
            }else if(a+b > target){
                --rr;
            }else{
                ++ll;
            }

        }

        return res;
    }

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); //how to sort Array
        List<List<Integer>> res = new ArrayList<>(); //Declare ArrayList
        int N = nums.length;//length of Array is an attribute

        for(int ii=0; ii<N-2; ++ii){
            List<List<Integer>> twos = two_sum(ii+1, 0-nums[ii], nums);
            if(ii>0 && nums[ii]==nums[ii-1]) continue;

            for(int jj=0; jj<twos.size(); ++jj){//length of ArrayList is Size
                //how to append number to ArrayList
                res.add(Arrays.asList(nums[ii], twos.get(jj).get(0), twos.get(jj).get(1))); //random access ArrayList          
            }
        }

        return res;

    }
}