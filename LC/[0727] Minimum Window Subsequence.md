> Naive solution (two pointer)+Greedy
* Time: S*(M+N) --> similar to DP solution
* find a starting point, always look for 1st next char in order to achieve min len

> Finite state machine strategy+Greedy

* preprocess next[ii][ch]: look right from position i, the nearest index of ch
* Time: S*N + (26*N)
  where next will take 26N, and we will do S*N look (S should be much smaller than M)


```cpp
int m = s1.size();
s1="#"+s1;
//declare state machine
int next[m+1][26];

//initialize state machine
for (int ch = 0; ch<26; ++ch) next[m][ch]=-1; //nothing after last char in s1
for(int ii=m-1; ii>=0; --i){
    for(int ch=0; ch<26; ++ch>){
        next[ii][ch] = next[ii+1][ch];
    }
    next[ii][s1[ii+1]-'a']=ii+1;
}

//identify starts
vector<int> start;
for(int i=1; ii<=m; ++ii){
    if(s1[ii]==s2[0]) start.push_back(ii);
}

for(int ii: start){
    int jj = ii-1;
    int flag=1;

    string ret = "";
    for(auto ch: s2){
        jj = next[jj][ch-'a'];
        if(jj==-1) {
            flag=0;
            break;
        }
    }
    if(flag){
        int len = jj-ii+1;
        if(ret=="" || len < ret.size()>){
            ret = s1.substr(ii, len);
        }
    }
}

return ret;

```



> DP III - two series counting/optimization
* Time - M*N