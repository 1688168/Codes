> Inputs:
+ books[ii]=[height, thickness]
+ shelf_width #max width a shelf can be
  
> Output:
=> min total shelf height

> Constraints:
1. books can be place to the shelf in sequencial order (do not sort)
2. each shelf can hold upto width less than "shelf_width"

> Analysis:
1. N=1000 -> we can do N^2
A: can we do DP:
  - single array with dp[ii] relating to some jj 
B: can we bruteforce by search?

dp[ii] = min total height with books ending @ ii
dp[ii] = dp[jj] + max_height_current_shelf
? what is jj candidates?

jj can be anything less than ii and total width cannot exceed threshold

> strategy: DP type II - Basic
1. for each ii as last book
2. try each jj (including ii) and maintain current_shelf_max_height and current_shelf_ttl_width
3. dp[ii] = min(dp[ii], dp[jj]+current_shelf_max_height)