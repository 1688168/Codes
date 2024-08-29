> dp[left][right]  

```c++
for(int ii=0; ii<N; ++ii){
    int ll=rod[ii];
    for(int left=0; left <=5000; ++left)
        for(int right=0; right <=5000; ++right>){
            if(dp[left][right]=true){
                dp[left+ll][right]=true;
                dp[left][right+ll]=true;
                if(left+ll==right) result => left+ll;
                if(right+ll==left) result => right+ll;
            }
        }
}
```

> A=B => A-B=0 => diff=0 (this reduces from two dimension to one dimension)  

dp[diff]: max(left) @ diff

```c++
    for(int ii=0; ii<N; ++ii){
        int ll = rod[ii];
        dp[diff+ll] => dp_old[diff]+ll; //adding to left
        dp[diff-ll] => dp_old[diff];//adding to right
    }
``