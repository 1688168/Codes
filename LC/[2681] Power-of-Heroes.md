### Observations
- min*max^2 of all group
- group means subset
- whenever we want to do something for min/max of subset or subsequence, sort first

0 1 2 3 4 5 6 7
x y z w p o o o

> min*max^2 * num_of_subsets

- when ii=3 is the max
z * 2^0 * nums[ii]^2
y * 2^1 * nums[ii]^2
x * 2^2 * nums[ii]^2

- when ii=4 is the max
w * 2^0 * nums[ii]^2

z * 2^1 * nums[ii]^2
y * 2^2 * nums[ii]^2
x * 2^3 * nums[ii]^2

A=
(z * 2^0 
+y * 2^1 
+x * 2^2) 

B=(z * 2^1
+y * 2^2 
+x * 2^3)

B=A*2

acc= acc*2

power_of_heros[ii]= power_of_hear[ii-1]+acc*2*nums[ii]^2+nums[ii]*nums[ii]^2



