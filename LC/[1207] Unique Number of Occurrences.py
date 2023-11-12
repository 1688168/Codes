class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n2cnt = collections.Counter(arr)
        unique_occurance = set(n2cnt.values())
        return len(unique_occurance) == len(n2cnt)
