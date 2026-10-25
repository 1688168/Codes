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