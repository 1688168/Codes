bool FindSumOfThree(vector<int> nums, int target)
{
   int N = nums.size();

   sort(nums.begin(), nums.end());
   for(int ii=0; ii<N-2; ++ii){
      int ll=ii+1, rr=N-1;
      while(ll<rr){
         int ttl=nums[ii]+nums[ll]+nums[rr];
         if(ttl==target){
            return true;
         }else if(ttl > target){
            --rr;
         }else{
            ++ll;
         }
      }

   }

   return false;
}