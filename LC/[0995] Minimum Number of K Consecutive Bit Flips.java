class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int N = nums.length;
        // events array tracks when a flip's effect expires
        int[] events = new int[N + 1];
        int count = 0; // num of required flip
        int flips = 0; // accumulated flip (including involuntary flips)
        
        for (int ii = 0; ii < N; ++ii) {
            flips += events[ii]; // update accumulated flips at current index ii
            
            // Logic:
            // If nums[ii] is 1 and flips is even (0) -> 1+0=1 (OK)
            // If nums[ii] is 0 and flips is odd (1)  -> 0+1=1 (OK)
            // If result is not 1, the bit is effectively 0 and needs a flip.
            if ((nums[ii] + flips % 2) == 1) continue; 
            
            // If we are here, current bit is effectively 0, so we must flip
            ++flips; 
            
            // Check if a window of size k fits
            if (ii + k - 1 >= N) return -1; 
            
            // Mark that this flip stops affecting the sequence at index ii + k
            events[ii + k] -= 1; 
            
            ++count; // Increment total operation count
        }

        return count;
    }
}