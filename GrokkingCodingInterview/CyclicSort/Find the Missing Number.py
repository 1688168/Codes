# Solution 0
 # why not go by math?
 def find_missing_number(nums):

  N=len(nums)
  ttl=sum(nums)

  ttl_expected= (N+1)*(N)//2


  return ttl_expected-ttl


# Solution 1 cyclic sort use while loop
def find_missing_number(nums):
  ii=0

  while ii < len(nums):
    if nums[ii] < len(nums) and nums[ii] != ii:
      idx=nums[ii]
      nums[ii], nums[idx] = nums[idx], nums[ii]
      continue
    ii += 1

  ii=0
  while ii < len(nums):
    if nums[ii] != ii:
      break
    ii += 1

  return ii

# solution 2 using for loop
def find_missing_number(nums):
  N=len(nums)
  for ii in range(N):
    while nums[ii] != ii:
      curr=nums[ii]
      if curr < N:
        nums[ii]=nums[curr]
        nums[curr]=curr
      else:
        break


  for ii in range(N):
    if ii != nums[ii]:
      return ii


  return -1
