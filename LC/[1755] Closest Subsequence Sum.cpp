/*
20240918
*/
class Solution {
    int ans=INT_MAX;
public:
    int minAbsDifference(vector<int>& nums, int goal) {
        int M = nums.size()/2;
        //partition to groupA and groupB
        vector<int> A(nums.begin(), nums.begin()+M);
        vector<int> B(nums.begin()+M, nums.end());

        vector<int> sortedSubsetSumsA = getSortedSubsetSums(A);
        vector<int> sortedSubsetSumsB = getSortedSubsetSums(B);

        bsearch(sortedSubsetSumsA, sortedSubsetSumsB, goal);
        
        return ans;
    }

    vector<int> getSortedSubsetSums(vector<int> & nums){
        int N = nums.size();
        vector<int> sums;

        //keep increment state as long as state is NOT exceeding required digits to hold nums.size(), this way we have all subsets for the digits
        for(int state=0; state < (1<<N); ++state){ //all bit combinations for the number of digits required to host the size of nums
            int tmp_sum=0;
            for(int ii=0; ii<32; ++ii){//try each bit of the 32 int
                if((state>>ii) & 1 && ii<N){//ii<N is not required as it won't be true and causing array out of bound
                    tmp_sum+=nums[ii];
                }
            }
            sums.push_back(tmp_sum);
        }   
        sort(sums.begin(), sums.end());
        return sums;

    }

    void bsearch(vector<int> & aa, vector<int> & bb, int goal){
        //a: sorted subset sums for group A
        //b: sorted subset sums for group B
        //we picked some from A and rests from B
        // given a subsetSum from A, do we have the complement sum from B?
        // if so, that could be a candidate s.t. subsetSumA+subsetSumB ~= goal
        // try all candidates and return the smallest one s.t. min(goal-sumA-sumB)

        for(auto a: aa){//for each subset sum a
            //find the first itt s.t. *itr+a~=goal
            auto itr = lower_bound(bb.begin(), bb.end(), goal-a);
            if(itr != bb.end()){
                ans=min(ans, abs(goal-a-*itr));
            }
            if(itr != bb.begin()){//if itr is NOT being, we have a prev
                ans=min(ans, abs(goal-a-*prev(itr)));
            }

        }
    }
  
};

//================================
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