from itertools import permutations

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Generate unique permutations and sort them.
        ordered = sorted(set(permutations(nums)))

        # Find the current permutation and choose the next.
        current = ordered.index(tuple(nums))
        next_idx = (current + 1) % len(ordered)

        # Update the original list in place.
        nums[:] = ordered[next_idx]