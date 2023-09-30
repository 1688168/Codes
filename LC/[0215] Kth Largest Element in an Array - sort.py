class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        1. sort: Nlog(N)
        2. heap: Space - O(K)
        3. quick-select - O(N) Avg
        4. binary search - 
        """
        ####
        # Sort solution: NlogN
        ####

        return sorted(nums)[len(nums)-k]
