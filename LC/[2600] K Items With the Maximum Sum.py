class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ttl=0

        if numOnes >= k:
            return k
        
        ttl += numOnes
        k -= numOnes

        if numZeros >= k:
            return ttl

        
        k -= numZeros

        if numNegOnes >= k:
            ttl -= k
            return ttl
        

        return -1