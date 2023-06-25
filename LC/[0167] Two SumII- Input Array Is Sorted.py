class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        N = len(numbers)
        ll, rr = 0, N-1
        while ll < rr:
            nl = numbers[ll]
            nr = numbers[rr]
            if nl+nr == target:
                return [ll+1, rr+1]
            if nl + nr > target:
                rr -= 1
                continue
            if nl + nr < target:
                ll += 1
                continue

        return ans
