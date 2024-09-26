using LL = long long;
class Solution {
   
public:
    unordered_map<int, vector<LL>> helper(vector<int>&nums){
        int n = nums.size();
        unordered_map<int, vector<LL>> Map;
        for(int state = 0; state < (1 << n); ++state){//python use combinations
            int cnt = __builtin_popcount(state);//c++ count how many 1 bits
            LL y = 0;
            for(int ii=0; ii<32; ++ii){               
               if((state >> ii) & 1) y+= (LL)nums[ii];
            }
            Map[cnt].push_back(y);
        }
        for(auto & x: Map){
            sort(x.second.begin(), x.second.end());
        }
        return Map;
    }

    int minimumDifference(vector<int>& nums) {
        int n = nums.size()/2;
        vector<int> nums1(nums.begin(), nums.begin()+n);//first half
        vector<int> nums2(nums.begin()+n, nums.end());//2nd half

        unordered_map<int, vector<LL>> Map2 = helper(nums2);
        LL sum = accumulate(nums.begin(), nums.end(), 0LL);
         LL ret = LLONG_MAX;//c++ largest long long
        //c++ use bit mask
        for(int state = 0; state < (1 << n); ++state){//python use combinations
            int cnt = __builtin_popcount(state);//c++ count how many 1 bits
            LL x = 0;
            for(int ii=0; ii<32; ++ii){  
                if((state >> ii) & 1) x+= (LL)nums1[ii];
            }

            int jj = n-cnt;
            auto iter = lower_bound(Map2[jj].begin(), Map2[jj].end(), sum/2-x);
            if(iter != Map2[jj].end()){
                LL y = *iter;
                ret = min(ret, abs(sum-2*(x+y)));
            }

            if(iter!=Map2[jj].begin()){
                iter = prev(iter);
                LL y = *iter;
                ret = min(ret, abs(sum-2*(x+y)));
            }

        }
        return ret;
    }
};

/*
+ First Half: 2^15 => ii, x (pick ii from first half with sum x)
+ Second Half: jj = n-ii, y 

x+y ~= total-(x+y)
-> total ~= 2(x+y)
-> y=total/2-x

if we have 2nd part depends on first part -> think of preprocess 2nd part and for each element from part1, binary search the 2nd part

* map[jj] = {y1, y2, ...}

ret = min(ret, abs(sum-2(x+y)))

> Complexity analysis
//preprocess group 2
+ O(2^n*n): + all combination - 2^n
            + sum for each combination - n

//group 1:
+ O(2^n) //all combination
+ O(2^n*log(2^n)) //binary search group 2 for each group 1 combination
*/

