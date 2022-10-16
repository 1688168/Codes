class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums)
    {
        int n = nums.size();
        int j = n-1;
        vector<int>rets(n);
        vector<int>count(32); //32 bit array indicate the current OR condition

        for (int i=n-1; i>=0; i--) //for each element in nums
        {
            for (int k=0; k<32; k++) //accumulate the bits into count
                count[k] += ((nums[i]>>k)&1);


            while (j>i && isOK(nums[j], count)) //can we take out num[jj] bits from counts and all positive bits still positive?  if so, we can remove nums[jj]
            {
                for (int k=0; k<32; k++)
                    count[k] -= ((nums[j]>>k)&1);
                j--;
            }

            rets[i] = j-i+1;
        }
        return rets;

    }

    bool isOK(int num, vector<int>&count)
    {
        for (int k=0; k<32; k++)
        {
            if (count[k] > 0 && (count[k] - ((num>>k)&1) <= 0))
                return false;
        }
        return true;
    }
};
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
