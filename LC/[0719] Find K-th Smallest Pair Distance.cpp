class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) 
    {
        sort(nums.begin(),nums.end());//not exceeding nlogn->sort
        int N=nums.size();
        
        //define the binary search upper/lower bound
        int left=nums[1]-nums[0];
        for (int i = 0; i <= N-2; ++i)//try all pairs, ending N-2
            left = min(left, nums[i+1] - nums[i]); //smallest distance
        
        int right=nums[N-1]-nums[0]; //largest distance
        int mid;
        
        while (left<right) //starting binary search -> O(32) loop
        {
            mid=left+(right-left)/2;
            int count=0;
            for (int i=0; i<N; i++) //O(N)
            {
                //O(logN)
                
                auto pos=upper_bound(nums.begin(),nums.end(), nums[i]+mid);
                count+= pos-1-(nums.begin()+i);
            }
            if (count<k)
                left=mid+1;
            else
                right=mid;
        }
        
        return left;
    }
};