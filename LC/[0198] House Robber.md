# <center><b><span style="color:orange">House Robber II</span></b></center>


> # <b><span style="color:purple">Analysis</span></b>  

> ### <b><span style="color:green">House Robber I</span></b>
* This is DP I as current status (max profit @ ii) purely depends on previous status @ ii-1
* in this case, previous status has two conditions. rob or noRob

> ### <b><span style="color:green">House Robber II</span></b>
* if we create a function to return house robber I
* consider rob 1st
  [R] N o o o [N]
        ^^^^^
        this part is house robber I
* consier not rob 1st
  [N] o o o o o o 
      ^^^^^^^^^^^
      this part is house robber I

> ### <b><span style="color:green">Strategy</span></b>

1. create a helper function solve house robber I
2. in the driver class, return max of case I or II