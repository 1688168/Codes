class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int N = nums.size();
        vector<int> events(N+1, 0);
        int count = 0; //num of required flip
        int flips = 0; //accumulated flip (including involuntary flips)
        for(int ii=0; ii<N; ++ii){
            flips += events[ii];//accumulated flips at ii
            if(nums[ii] + flips%2==1) continue;//already 1 -> noop
            ++flips;
            if(ii+k-1 >= N) return -1; //ii+k-1 is the last bit in the interval
            events[ii+k] -= 1;//ii+k is the 1st bit after the interval
            ++count;//mandatory flip
        }

        return count;
    }
};


// ### Given
// * nums[ii]:
// * k-bit flip: x 123456k xxxx
// * flip subarray of len k: 0->1, 1->0

// ### Ask
// * min k-bit flip required -> no 0
// * -1 if not possible

// ### Analysis
// * subarray of len=k -> interval of len k
// * when you need to flip a bit but the len from the bit to th end is less than k -> return -1
// * whenever you notice we need to do interval addition/substraction/... -> sweepline
// * N=3x10^4