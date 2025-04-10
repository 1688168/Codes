class Solution {
    public:
        int deleteAndEarn(vector<int>& nums) {
            if(nums.size()==0) return 0;
            sort(nums.begin(), nums.end());
            int M = nums.back();
            vector<int> gain(M+1, 0);
            for(auto x: nums) gain[x] += x;
    
            int p=0; //p[ii]: max gain by earning ii 
            int q=0;//q[ii]: max gain by not earning ii
            for(int ii=1; ii<=M; ++ii){//traversing each number, house robber I
                int p2=p, q2=q;
                p = q2 + gain[ii];
                q = max(p2, q2);
            }
    
            return max(p, q);
            
        }
    };
    /*
    * we want to delete a value and remove v+1, v+2
    * so this array actually is sortable as the result is the same after the sort
    */