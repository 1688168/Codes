dp[i][j]: minimum sum of a falling path with non-zero shifts from 1st row to (i, j)
dp[i][j]=dp[i-1][k]+grid[i][j]

* to avoid repeated seaching for dp[i-1][k], find top and second in one scan.
* -> if min is same ii, use 2nd-min, otherwise, use min
* or you can sort
* 