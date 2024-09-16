class Solution {
    int ret = INT_MAX;
public:
    int minAbsDifference(vector<int>& nums, int goal) {
        int m = nums.size()/2; //num in groupA
        //int n = nums.size()-m; //num in groupB

        vector<int> nums1(nums.begin(), nums.begin()+m);//c++ initialize vector from subarry of another vector
        vector<int> nums2(nums.begin()+m, nums.end());
        vector<int> a = getSubSetSums(nums1);
        vector<int> b = getSubSetSums(nums2);

        bs(a, b, goal);
        //bs(b, a, goal); //<< this is not required

        return ret;
    }

    //the most efficient way to get all subset sum given a list
    vector<int> getSubSetSums(vector<int>&nums){//c++ get all subset sum
        vector<int> sums;
        int m = nums.size();
        for(int state=0; state<(1<<m); ++state){ //from 0000->1111
            int sum=0;
            for(int ii=0; ii<32; ++ii){//collect a subset sum
                if((state >>ii)&1) sum+=nums[ii]; 
            }
            sums.push_back(sum);
        }
        sort(sums.begin(), sums.end());
        return sums;
    }

    void bs(vector<int> & a, vector<int> &b, int goal){
        for(int x: a){ //given a subset sum from groupA
            auto iter = lower_bound(b.begin(), b.end(), goal-x); //binary search complement from groupB
            /*
            we are looking for sumA+sumB~goal
            where sumA is sum of elements picked in groupA
                  sumB is sum of elements picked in groupA
            min(diff)=sumA+SumB-goal
            */
            if (iter !=b.end()){//means we have a solution
                ret = min(ret, abs(x+*iter - goal));
            }
            if(iter!=b.begin()){
                ret = min(ret, abs(x+ *prev(iter) - goal));
            }
        }
    }
};