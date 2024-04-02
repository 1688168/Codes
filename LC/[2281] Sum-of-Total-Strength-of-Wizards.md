# Required Skills:

1. monotonic stack (prev_smaller_equal/next_smaller)
2. presum
3. special presum

# Analysis

a x x x x ii x x x b

nums[ii]: the weakest wizard strength
x=ii-a
y=b-ii
nums[a]: pre_smaller_equal (vs nums[ii])
nums[b]: next_smaller

Let ret[ii] be the total strength of all subarraies where nums[ii] is the weakest wizard

ret[ii] = (left*(b-ii) + mid*(x*y) + right*(ii-a))\* nums[ii]

left = nums[a+1]*1 + nums[a+2]*2 + nums[a+3]*3 + nums[a+4]*4
mid = nums[ii]* x*y
right = nums[ii+1] * 3 + nums[ii+2]*2 + nums[ii+3] \* 1

let presum2 = nums[1] * 1 + nums[2]*2 + ... + nums[n]\*N

presum2[ii]-presum2[a]=nums[a+1]_(a+1)+nums[a+2]_(a+2)+nums[a+3]_(a+2) + nums[a+4]_(a+4)
= left + presum[a+1:ii]\*a

## => left = presum2[ii]-presum2[a] - presum[a+1:ii]\*a

presum2[b-1]-presum2[ii] = nums[ii+1]_(ii+1)+nums[ii+2]_(ii+2)+nums[ii+3]*(ii+3)
= nums[ii+1]*b+nums[ii+2]*b + nums[ii+3]*b - right

## => right = presum[ii+1: b]\*b - (presum2[b-1]-presum2[ii])

> # 20231015

"""
total_strength = weakest_wizard_strength \* sum(strength_in_subarray)

      strength > 10^5 => nlog(n) or O(N)
      all_subarray -> O(N^2) => X

      for each ii as weakest wizard. calc all subarrays's ttl strength with strength[ii] as weakest
      0 1 2 3 4 5 6 7 8
      x x x x x x x x x
              i
      ^
      a               b  #(a,b)=(prev_saller_equal, next_smaller)

      x = ii-a
      y = b-ii

      subarray_strength = left + mid + right

## Regarding Left

      left = (nums[a+1] * 1 + nums[a+2] * 2 + nums[a+3]*3 + nums[a+4] * 4)*nums[ii]*y
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              what we want left

      mid = x*y* nums[ii]*nums[ii]   #two nums[ii] here, 1st one is for sum, 2nd one is the weakest strength
      right = (nums[b-1] * 1 + nums[b-2]*2 + nums[b-3]*3) * nums[ii]*x
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               what we want right

      let presum2 = nums[1]*1 + nums[2]*2 + ... + nums[k]*k
      presum2[ii-1]-presum2[a]
          = nums[a+1]*(a+1) + nums[a+2]* (a+2)+ nums[a+3]*(a+3) + nums[a+4]*(a+4)
          = "what we want left" + (presum[ii-1]-presum[a])*a

    ==================================================================
      "what we want left" = presum2[ii-1]-presum2[a]- (presum[ii-1]-presum[a])*a
    ==================================================================

## Regarding Rigth

      presum2[b-1]-presum2[ii] =
        nums[ii+1]*(b-ii-1)+nums[ii+2]*(b-ii-2) + nums[ii+3]*(b-ii-3)
      = nums[b-3]*(b-ii-1)+nums[b-2]*(b-ii-2)+nums[b-1]*(b-ii-3)
      = nums[b-1]*(b-ii-3)+nums[b-2]*(b-ii-2)+nums[b-3]*(b-ii-1)

      = nums[b-1]*b + nums[b-2]*b+nums[b-3]*b - "what we want right"
      = (presum[b-1]-presum[ii])*b - "what we want right"

    ====================================================================
      => "what we want right" = (presum[b-1]-presum[ii])*b-presum2[b-1]+presum2[ii]
    ====================================================================

      ttl_strength =
        "what we want left"*nums[ii]*y
      + mid*x*y
      + "what we want right"*nums[ii]*x

      + prepare prev/next smaller to identify range of weakest strength
      + prepare presum
      + prepare presum2

      """
