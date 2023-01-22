#include <deque>
#include <vector>
vector<int> FindMaxSlidingWindow(vector<int>& nums, int windowSize)
{
    deque<int> dq;
    vector<int> res;
    if (windowSize > nums.size())
    {
        windowSize = nums.size();
    }
    for(int ii=0; ii<nums.size(); ++ii){//traversing the array
        while(!dq.empty() && nums[ii] > nums[dq.back()]){//for each n in nums, if 
            dq.pop_back();
        }
        dq.push_back(ii);

        if(ii >= windowSize-1){
            res.push_back(nums[dq[0]]);
        }

        while(!dq.empty() && (ii+1-windowSize>= dq.front())){
            dq.pop_front();
        }
    }
    
    return res;
}