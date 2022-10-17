from functools import lru_cache
def can_partition(num, sum):
  N=len(num)

  @lru_cache(None)
  def dp(st, target):
    if target==0: return True
    if st >= N or target < 0: return False
    tke=dp(st+1, target-num[st])
    ntk=dp(st+1, target)

    return tke or ntk

  return dp(0, sum)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
