class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for(var nn: nums){
            int idx = Collections.binarySearch(list, nn);
            if(idx<0) idx = -idx-1;
            if(idx >= list.size()){
                list.add(nn);
            }else{
                list.set(idx, nn);
            }
        }
        return list.size();
    }
}

    // int idx = Collections.binarySearch(list, x);