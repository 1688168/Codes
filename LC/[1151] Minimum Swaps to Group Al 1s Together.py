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
