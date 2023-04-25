class Solution:
    def sumOfMultiples(self, n: int) -> int:
        _sum=0
        for nn in range(1, n+1):
            if nn % 3 == 0 or nn % 5 == 0 or nn % 7 == 0:
                _sum += nn
        
        return _sum
        