def find_missing_numbers(nums):
  missingNumbers = []
  ii=0
  while ii < len(nums):# 2,3, 2, 1
    if nums[ii] != nums[nums[ii]-1]:# 2, 3: (3, 2, 2, 1) (2, 2, 3, 1)
      curr=nums[ii]
      nums[ii], nums[curr-1]=nums[curr-1], nums[ii]
      continue

    ii += 1


  ii=0
  while ii < len(nums):
    if nums[ii]-1 != ii:
      missingNumbers.append(ii+1)
    ii+=1


  return missingNumbers
