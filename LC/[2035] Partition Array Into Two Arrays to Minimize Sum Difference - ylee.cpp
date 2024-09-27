/*
Inputs:
+ nums[ii]: an int
+ nums.size()=2N
+ partition nums into G1, G2
  s.t. diff=abs(sum(G1)-sum(G2))
  -> find min diff

note: 
* to consider 0/1 knapsack, nums[ii] need to be positive and cannot be too big (like 1000)
* whenever we partition something to two groups -> total=sum(G1)+sum(G2)
* when considering bruteforce (exhausted method), can we partition the nums in half, and bruteforce G1 and binary search on G2

Strategy:
1. partition in half g1, g2
2. build a subset of size n where we select x entry from g1, n-x entry from g2
2. diff = (total-(x+y)) - (x+y)
        = total - 2*(x+y)
   min(diff) => total ~ 2*(x+y)
                total/2-x ~ y <<<< search g2 this value
2. build map1 = (cnt, [all combination sum])
         map2 = (n-cnt, [all combination])

*/

using LL = long long;
class Solution {
public:
    LL ans = LLONG_MAX;
    int minimumDifference(vector<int>& nums) {
        int n = nums.size()/2;
        vector<int> g1(nums.begin(), nums.begin()+n);
        vector<int> g2(nums.begin()+n, nums.end());

        unordered_map<int, vector<LL>> A = getAllSum(g1);
        unordered_map<int, vector<LL>> B = getAllSum(g2);

        //for each A, binary search B
        LL ttl = accumulate(nums.begin(), nums.end(), 0LL);
        bsearch(A, B, n, ttl);
        return ans;
    }

    void bsearch(unordered_map<int, vector<LL>> & A, 
    unordered_map<int, vector<LL>> & B, int n, LL ttl){

        for(auto & x: A){ //for each entry in A
            int cnt = x.first;
            vector<LL> & aa = x.second;
            vector<LL> & bb = B[n-cnt];
            for(auto z: aa){
                auto iter = lower_bound(bb.begin(), bb.end(), ttl/2-z);
                if(iter != bb.end()){
                    ans = min(ans, abs(ttl - 2*(z + *iter)));
                }
                if(iter != bb.begin()){
                    ans = min(ans, abs(ttl - 2*(z+*prev(iter))));
                }
            }
           
        }

    }

    unordered_map<int, vector<LL>> getAllSum(vector<int> & nums){
        //get mapped combination sum
        int sz = (1<<nums.size());
        unordered_map<int, vector<LL>> map;
        for(int state=0; state < sz; ++state){
            int cnt = 0;
            LL acc = 0;
            for(int jj=0; jj<32; ++jj){
                if((state>>jj) & 1){
                    acc += nums[jj];
                    cnt += 1;
                }
            }

            map[cnt].push_back(acc);
        }
    
        //need to sort
        for(auto & x: map){
            sort(x.second.begin(), x.second.end());
        }

        return map;
    }
};