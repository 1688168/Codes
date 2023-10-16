### Observations
- min*max^2 of all group
- group means subset
- whenever we want to do something for min/max of subset or subsequence, sort first


0 1 2 3 4 5 6 7
x y z w p o o o


min*max^2 * num_of_subsets

ii
0: when x is the max
   acc=0           
 + x*x^2   # min is x as well

1: when y is the max
   x*y^2 * 2^0   # min is x 
 + y*y^2   # min is y  

2: when z is the max

   x*z^2 * 2   # min is x
   y*z^2 * 1   # min is y
   z*z^2       # min is z

3: when w is the max
   x*w^2 * 2^2 # min is x
   y*w^2 * 2   # min is y
   z*w^2 * 1   # min is z
   w*w^2       # min is w

...

when ii = kk
power of heros @ kk

+ kk*kk^2

