class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int ii = 0; ii < nums.length - 2; ii++) {
            // Reusing a fixed value would produce the same triplets.
            if (ii > 0 && nums[ii] == nums[ii - 1]) {
                continue;
            }

            List<List<Integer>> pairs = twoSum(nums, ii, -nums[ii]);
            for (List<Integer> pair : pairs) {
                res.add(Arrays.asList(pair.get(0), pair.get(1), nums[ii]));
            }
        }

        return res;
    }

    private List<List<Integer>> twoSum(int[] nums, int idx, int target) {
        int ll = idx + 1;
        int rr = nums.length - 1;
        List<List<Integer>> res = new ArrayList<>();

        while (ll < rr) {
            int aa = nums[ll];
            int bb = nums[rr];

            if (aa + bb == target) {
                res.add(Arrays.asList(aa, bb));
                ll++;
                rr--;
            } else if (aa + bb > target) {
                rr--;
            } else {
                ll++;
            }

            // Skip previously considered values to avoid duplicate pairs.
            while (rr < nums.length - 1 && rr > ll && nums[rr] == nums[rr + 1]) {
                rr--;
            }
            while (ll > idx + 1 && ll < rr && nums[ll] == nums[ll - 1]) {
                ll++;
            }
        }

        return res;
    }
}




//----------------
class Solution {
    private List<int[]> twoSum(int[] nums, int target, int idx){
        List<int[]> pairs = new ArrayList<>();

        int ll = idx + 1;
        int rr = nums.length -1;
        while(ll < rr){
            int a = nums[ll];
            int b = nums[rr];

            if(a+b == target){
                pairs.add(new int[]{a, b});
                ++ll;
                --rr;
                while(ll<rr && nums[ll]==nums[ll-1]) ++ll;
                while(ll<rr && nums[rr]==nums[rr+1]) --rr;
            }else if(a+b > target){
                rr-=1;
            }else{
                ll+=1;
            }


        }

        return pairs;
    }
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); //java sort int array. 
        int N = nums.length;

        List<List<Integer>> res = new ArrayList<>();

        //try each num as the first of triplet
        for(int ii=0; ii< N-2; ++ii){
            if((ii > 0) && nums[ii]==nums[ii-1]) continue; //skip duplicates
            if(nums[ii] > 0) break;

            var pairs = twoSum(nums, -nums[ii], ii);
            for(var pair: pairs){
                res.add(Arrays.asList(nums[ii], pair[0], pair[1])); //how to instanciate Java List
            }
        }

        return res;
    }
}