class Solution {
    public int singleNumber(int[] nums) {
        int xx = 0;
        for(var nn: nums) xx ^= nn;
        return xx;
    }
}