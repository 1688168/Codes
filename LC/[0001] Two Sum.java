class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int ii=0; ii<nums.length; ++ii){
            if(map.containsKey(target-nums[ii])) return new int[]{ii, map.get(target-nums[ii])};
            map.put(nums[ii], ii);
        }

        return new int[2];
    }
}