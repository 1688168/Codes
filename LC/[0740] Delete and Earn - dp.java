class Solution {
    public int deleteAndEarn(int[] nums) {
        int N = nums.length;
        if(N==0) return 0;
        if(N==1) return nums[0];
        Arrays.sort(nums);
        int M = nums[N-1]; //the max value in nums

        //declare an array from 0 to M (including)
        int[] arr = IntStream.range(0, M+1).map(ii -> 0).toArray();

        for(var x: nums) arr[x]+=x;

    
        int pick = arr[0];
        int skip = 0;

        //now we have transformed the problem into house robber problem
        for(int ii=1; ii<=M; ++ii){
            int tmpPick=pick;
            int tmpSkip=skip;
            skip = Math.max(tmpPick, tmpSkip);

            pick = arr[ii] + tmpSkip;
        }

        return Math.max(pick, skip);
    }
}

/*
> What is house Robber?
> Problem statement
* given nums
* max profit
> Constrains
* if ii is taken, nums[ii] +/- 1 then is removed
* whenever current state limits future state -> house robber
* in house robber, house index determines the current state
* in "Delete and Earn", value determins the current state
-> since array index play no role in pick or skip -> the array is sortable
-> in house robber, array index matters -> NOT sortable
* 
* 
*/