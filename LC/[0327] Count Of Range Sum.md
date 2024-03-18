> when you see range sum -> get presum

*  lower <= sum[ii:jj] <= upper  
-> lower <= presum[jj]-presum[ii-1] <= upper   
=> presum[jj] >=lower + presum[ii-1]   --- A
=> presum[jj] <= upper + presum[ii-1]  --- B
=> ii < jj
A: count of larger number after self (ii-1)
B: count of smaller number after self (ii-1)