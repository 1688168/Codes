> problem statement
* partition string into k substrings <<----- DP IV hint
* each substrings is a palindrome
* you can change some chars 
=> min char to change

> Analysis
* N=100
* we see a hint for DP IV

> DP IV
dp[ii][kk]: min num changes for nums[:ii+1] with kk partitions so all k substrings are palindrom
dp[ii][kk]=min(dp[ii][kk], dp[jj-1][kk-1]+x) for jj in kk-1, ii

for(int ii=1; ii<=n; ++ii){
    for(int kk=1; kk<=min(ii, k); ++kk){
        for(int jj=kk; jj<=ii; ++jj){
            dp[ii][kk] = dp[jj-1][kk-1] + X;
        }
    }
}

--> return dp[N-1][k];