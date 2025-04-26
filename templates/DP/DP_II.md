* need to loop through previous state to determine current state
[pattern]
```
dp[ii][jj][kk]
for ii=
    for jj=
        for kk=
            for prevState = ...
                dp[ii][jj][kk] = max(dp[prevState]) <<<this could be optimized to reduce one layer of looping
```