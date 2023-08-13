using LL=long long;
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        /*
        * subarray (continuous): abs(diff of any pair) <= 2 ===> (max-min) <=2
        * if we have a window (ll, rr) were (max-min) <= 2
        * -> number of continuous array which ends on rr -> rr-ll+1
        * ll=rr=0
        * expand rr and accumulate count of continuous array (ends on rr)
        * when the subarray[ll:rr] disqualified, increment ll until subarray[ll:rr] qualify again   

        * to maintain sliding window max/min -> deque
        * Time: O(N)
        * Space:O(N)
        */
        deque<int> dq_max, dq_min;
        int ll=0, rr=0, N=nums.size();
        LL ans=0;
        for(rr=0; rr < N; ++rr ){//for each subarray ending with rr
            //find min/max in the subarray
            //shrink the subarray until (max-min) <=2
            //count, accumulate the number      
            while(!dq_max.empty() && nums[rr] > nums[dq_max.back()]) dq_max.pop_back();
            dq_max.push_back(rr);
            
            while(!dq_min.empty() && nums[rr] < nums[dq_min.back()]) dq_min.pop_back();
            dq_min.push_back(rr);

            while(!dq_max.empty() && !dq_min.empty() && (nums[dq_max.front()] - nums[dq_min.front()]) > 2){
         
                while(!dq_max.empty() && dq_max.front() <= ll) dq_max.pop_front();
                while(!dq_min.empty() && dq_min.front() <= ll) dq_min.pop_front();
                ++ll;
            }  
            ans += (rr-ll+1);
        }

     return ans;
    }
};