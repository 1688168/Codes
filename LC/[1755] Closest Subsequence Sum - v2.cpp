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
        //bs(b, a, goal);

        return ret;
    }

    // vector<int> getSubSetSums(vector<int>&nums){//c++ get all subset sum
    //     vector<int> sums;
    //     int m = nums.size();
    //     for(int state=0; state<(1<<m); ++state){ //from 0000->1111
    //         int sum=0;
    //         for(int ii=0; ii<32; ++ii){//collect a subset sum
    //             if((state >>ii)&1) sum+=nums[ii]; 
    //         }
    //         sums.push_back(sum);
    //     }
    //     sort(sums.begin(), sums.end());
    //     return sums;
    // }
    
    //the best way to get sorted subset sums?
    // get subset sum from a list using merge sort
    vector<int> getSubSetSums(vector<int> & nums){
        /* merge sort the following two lists:
        sums[ii] = {a1, a2, ..., ak}
        sums'[jj]  {a1+nums[ii], a2+nums[ii], ..., ak+nums[ii]}
        sums = {b1, b2, ..., b2k}
        */
        vector<int> sums({0});//notice this need to be initialized with zero
        for(int x: nums){ //for each new number
            int ii=0, jj=0;
            int n = sums.size();
            vector<int>temp;
            while (ii<n && jj<n){//merge two sorted lists
                if(sums[ii] < sums[jj]+x){
                    temp.push_back(sums[ii]);
                    ++ii;
                }else{
                    temp.push_back(sums[jj]+x);
                    ++jj;
                }
            }

            while(ii<n){
                temp.push_back(sums[ii]);
                ++ii;
            }

            while(jj<n){
                temp.push_back(sums[jj]+x);
                ++jj;
            }

            sums = temp;
        }
        return sums;
    }

    void bs(vector<int> & a, vector<int> &b, int goal){
        for(int x: a){ //given a subset sum from groupA

            //so x+goal-x=goal -> find first number in b s.t. x+y >= goal
            auto iter = lower_bound(b.begin(), b.end(), goal-x); //binary search complement from groupB
            /*
            we are looking for sumA+sumB~goal
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