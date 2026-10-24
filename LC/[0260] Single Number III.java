class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for(var nn: nums) xor ^= nn;

        int mask = xor&(-xor);
        int a=0;
        int b=0;
        for(var nn: nums){
            if((nn&mask) != 0){
                a^=nn;
            }else{
                b^=nn;
            }
        }

        return new int[]{a, b};
    }
}