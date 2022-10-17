def can_partition(num, sum):
  N=len(num)
  dp=[False]*(sum+1)

  for ii in range(sum+1):
    if ii == num[0]: dp[ii]=True

  dp[0]=True

  for ii in range(1, N):
    for jj in reversed(range(sum+1)):
      dp[jj]=dp[jj] or (dp[jj-num[ii]] if jj >=num[ii] else False)


  return dp[-1]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
