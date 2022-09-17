"""
Conditional probability:
A => B1, B2
     B1 => C1, C2
     B2 => C1, C2

what's the probability from A->C1

Two strategies:
1. recursion
  f(A): A->C1
  A->B1->C1 0.3*0.3
  A->B2->C1 0.7*0.3

f(A->c1) = f(A->B1)*f(B1->C1)+f(A->B2)*f(B2, C1)

2. DP
dp[C1]: the probability reaching C1
      =dp[B1]*f(B1->C1) + dp[B2]*f(B2->C1)
       dp[A]*f(A->B1)     dp[A]*f(A->B2)
dp[A]=1 (starting point)

dp1[ii][jj] //after 1 move, the probabily of having hourse on (ii, jj)
dp2[ii][jj] = sum(dp1[x][y]*1/8) //from previous move, who can reach (ii, jj)


dp[x][y] => dp2[ii][jj] += dp1[x][y]*1/8
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        N=n
        # defines NXN array
        dp1 = [[0]*N for _ in range(N)]


        dp1[row][column]=1

        dirs=[(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


        def is_valid(x, y):
            if x<0 or y < 0 or x >= N or y >= N: return False
            return True

        for kk in range(k):
            dp2 = [[0]*N for _ in range(N)]
            for ii in range(N):
                for jj in range(N):

                    for dx, dy in dirs:
                        nx, ny=ii+dx, jj+dy
                        if is_valid(nx, ny):
                            dp2[ii][jj] += dp1[nx][ny]*1/8
            dp1=dp2[:]

        res=0
        for ii in range(N):
            for jj in range(N):
                res += dp1[ii][jj]
        return res
