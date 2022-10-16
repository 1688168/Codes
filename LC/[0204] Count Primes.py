class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0 #edge case

        # process of elimination, we first list out all the outcomes as True
        # except those you already know they are flase ( 0, 1)
        is_prime=[False, False] + [True]*(n-2)

        for p in range(2, int(sqrt(n))+1):
            if is_prime[p]:
                for p in range(p*p, n, p):
                    is_prime[p]=False

        return sum(is_prime)
