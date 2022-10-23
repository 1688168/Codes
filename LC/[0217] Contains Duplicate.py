# one liner
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False

# sol 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        for n in nums:
            if n in visited: return True
            visited.add(n)
        return False
