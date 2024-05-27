class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count1=0, count2=0;
        //count1: upto now, the longest consecutive 1s ending here without flip
        //count2: upto now, the longest consecutive 1s ending here, with 1 flip
        int ret=0;
        for(auto x: nums){
            if(x==0){
                count2 = count1+1;
                count1=0;
            }else{
                ++count2;
                ++count1;
            }
            ret = max(ret, count2);
        }
        return ret;
    }
};