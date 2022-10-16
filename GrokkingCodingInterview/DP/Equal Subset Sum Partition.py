# Top-down approach
from functools import lru_cache
def can_partition(num):
  N=len(num)
  ttl=sum(num)
  if ttl%2 != 0: return False

  target=ttl//2

  @lru_cache(None)
  def dp(st, target):
    if target==0:
      return True
    if st >=N or target < 0:
      return False

    return dp(st+1, target) or dp(st+1, target-num[st])


  return dp(0, target)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


# bottom up approach
def can_partition(num):
  N=len(num)

  ttl=sum(num)
  if ttl%2==1: return False
  target=ttl//2

  dp=[[False for _ in range(target+1)] for _ in range(N)]

  # dp[ii][jj]: True/False can sum to jj using up to ii elements
  for ii in range(target+1):
    dp[0][ii] = True if ii==num[0] else False

  for ii in range(N):
    dp[ii][0]=True

  for ii in range(1, N):
    for jj in range(1, target+1):
      dp[ii][jj] = dp[ii-1][jj] or ((dp[ii-1][jj-num[ii]]) if jj >= num[ii] else False)

  return dp[-1][-1]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


# one dimention DP?
def can_partition(num):
  N=len(num)

  ttl=sum(num)
  if ttl%2==1: return False
  target=ttl//2

  dp=[False for _ in range(target+1)]

  # dp[ii][jj]: True/False can sum to jj using up to ii elements
  for ii in range(target+1):
    dp[ii] = True if ii==num[0] else False

  dp[0]=True

  for ii in range(1, N):
    for jj in reversed(range(1, target+1)):
      dp[jj] = dp[jj] or ((dp[jj-num[ii]]) if jj >= num[ii] else False)

  return dp[-1]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
