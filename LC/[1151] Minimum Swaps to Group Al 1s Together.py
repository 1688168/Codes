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
