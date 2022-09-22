# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 2: return 0
#         mm={}
#
#         for p in range(2, int(sqrt(n))+1):
#             if p not in mm:
#                 for m in range(p*p, n, p):
#                     mm[m]=1
#
#         return n-len(mm)-2

#
#
#

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0

        is_prime=[False, False] + [True]*(n-2)

        for p in range(2, int(sqrt(n))+1):
            if is_prime[p]:
                for p in range(p*p, n, p):
                    is_prime[p]=False

        return sum(is_prime)



        
