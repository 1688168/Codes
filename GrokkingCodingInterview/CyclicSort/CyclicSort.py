def cyclic_sort(nums):
  N=len(nums)
  for ii in range(N):
    while nums[ii]!= ii+1:
      curr=nums[ii]
      nums[ii]=nums[curr-1]
      nums[curr-1]=curr
  return nums
