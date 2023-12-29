##############
# 20231229
##############
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        - shortest: BFS
        - N: 10^4 --> O(N)?
        => "length" of the unsorted subarray

        ** bruteforce: 
        1. all subarray: O(N^2) -- A
        2. is sorted: O(N)  -- B
        --> A*B
        ** ideas0:
        * the beginning index of the violation subarray
        -> first index smaller than max_so_far from the left

        * the ending index of the violation subarray
        -> first index greater than min_so_far from the right

        =>  end_index-begin_index+1

        ** ideas1:
        x x x x x x x
        * find first ii who's next smaller is not @ N
        * find last ii who's prev greater is not @ -1
        * the distance is the answer

        - the beginning index is the first ii who's next smaller is not @ N
        - the ending index is the last ii who's prev greater is not @ -1

        ** next smaller/prev smaller/greater -> two monotonic stack
        1. build next_smaller
        2. build prev_greater

        """
        N = len(nums)

        # find first index that nums[st] > min_so_far from the right. return 0 if st==N
        min_so_far = nums[-1]
        st = N
        for ii in reversed(range(N)):
            nn = nums[ii]
            if nn > min_so_far:
                st = ii

            min_so_far = min(min_so_far, nn)

        if st == N:
            return 0

        # find last index that is smaller than max_so_far from the left
        ed = -1
        max_so_far = nums[0]

        for ii, nn in enumerate(nums):
            if nn < max_so_far:
                ed = ii

            max_so_far = max(max_so_far, nn)

        return ed-st+1


######################
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        1. find index of the right most number that is less than max on it's left 
        2. find index of the left most number that is greater than min on it's right 
        3. the dist btn above two is the answer
        """
        # find the rigt most number that is less than the max on it's left
        N = len(nums)
        MXN = -math.inf
        rmni = 0
        for ii, vv in enumerate(nums):
            if vv < MXN:
                rmni = ii

            MXN = max(MXN, vv)

        MNN = math.inf
        lmni = N-1
        for ii in reversed(range(N)):
            vv = nums[ii]
            if vv > MNN:
                lmni = ii
            MNN = min(MNN, vv)

        return rmni-lmni+1 if rmni-lmni > 0 else 0
