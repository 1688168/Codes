#############
# 20240405
#############
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        - data[ii]: binary
        -> min swaps 

        """
        # edge cases:
        window_sz = sum(data)  # T: N
        if window_sz <= 1:
            return 0

        data = [0]+data
        N = len(data)
        presum = [0]  # space: N
        for ii, nn in enumerate(data[1:]):  # T: N
            presum.append(nn+presum[ii])

        ll, rr = 1, window_sz-1
        min_zero = math.inf
        for rr in range(window_sz, N):  # T: N
            min_zero = min(min_zero, window_sz-presum[rr]+presum[ll-1])
            ll += 1
        return min_zero
#############
# 20240107
#############


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        group all 1s together
        1. count how many ones
        2. sliding window with the lengh of ttl 1s and see how many zeros we need to fill
        3. output global min zeros need fill
        """
        ones = sum(data)  # count of all ones
        N = len(data)  # get size of the array

        zero_cnt = 0  # num of swap required
        mnz = math.inf
        for ii, nn in enumerate(data):
            if nn == 0:
                zero_cnt += 1
            if ii-ones >= 0 and data[ii-ones] == 0:
                zero_cnt -= 1
            if ii >= ones-1:
                mnz = min(mnz, zero_cnt)

        return mnz


#############
# 20230926
#############
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        N = len(data)
        if window_size == 0 or window_size == N:
            return 0
        min_swap = num_swap = window_size-sum(data[:window_size])

        for ii in range(window_size, N):
            if data[ii] == 0:
                num_swap += 1

            """
            0 1 2 3
            0 1 0 1
            ^   ^ 
              ^   ^
            """
            if data[ii-window_size] == 0:
                num_swap -= 1
            min_swap = min(min_swap, num_swap)
        return min_swap


################################
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_of_ones = sum(data)  # Time: O(N)
        N = len(data)
        min_swap = N
        num_of_swaps = 0
        for ii in range(num_of_ones):  # window size
            if data[ii] == 0:
                num_of_swaps += 1

        min_swap = min(min_swap, num_of_swaps)

        for ii in range(num_of_ones, N):
            if data[ii] == 0:
                num_of_swaps += 1
            if data[ii-num_of_ones] == 0:
                num_of_swaps -= 1
            min_swap = min(num_of_swaps, min_swap)

        return min_swap
