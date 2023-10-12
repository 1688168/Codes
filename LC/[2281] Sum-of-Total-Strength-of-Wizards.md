# Required Skills:

1. monotonic stack (prev_smaller_equal/next_smaller)
2. presum
3. special presum

# Analysis

0 1 2 3 4 5 6 7 8 9 0 1
a i b
x x a x x x x x x x x x
1 1 1 1 1  
 1 1 1 1  
 1 1 1
1 1
1  
 1 1 + 4
1 1 1 +4
1 1 1 1 + 4

nums[ii]: the weakest wizard strength
x=ii-a
y=b-ii
nums[a]: pre_smaller_equal (vs nums[ii])
nums[b]: next_smaller
Let ret[ii] be the total strength of all subarraies where nums[ii] is the weakest wizard

ret[ii] = (left + mid + right)\* nums[ii]

left = nums[a+1]*1 + nums[a+2]*2 + nums[a+3]*3 + nums[a+4]*4
mid = nums[ii]* x*y
right = nums[ii+1] * 3 + nums[ii+2]*2 + nums[ii+3] \* 3

let presum2 = nums[1] * 1 + nums[2]*2 + ... + nums[n]\*N

presum2[ii]-presum2[a]=nums[a+1]_(a+1)+nums[a+2]_(a+2)+nums[a+3]_(a+2) + nums[a+4]_(a+4)
= left + presum[a+1:ii]*a
=> left = presum2[ii]-presum2[a] - presum[a+1:ii]*a

presum2[b]-presum2[ii] = nums[ii+1]_(ii+1)+nums[ii+2]_(ii+2)+nums[ii+3]*(ii+3)
= nums[ii+1]*b+nums[ii+2]*b + nums[ii+3]*b - right
=> right = presum[ii+1: b]\*b - (presum2[b]-presum2[ii])
