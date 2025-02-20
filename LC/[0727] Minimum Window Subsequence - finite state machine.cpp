class Solution {
    public:
        string minWindow(string s1, string s2) {
            //min substring of s1 s.t. s2 is a subsequence.
    
            int const m = s1.size();//take s1 measurement
            s1="#"+s1;//insert dummy
    
            //declare state machine
            int next[m+1][26];//index of ch in s1 after s1[ii]
    
            //initialize state machine
            for (int ch = 0; ch<26; ++ch) next[m][ch]=-1; //nothing after last char in s1
    
            for(int ii=m-1; ii>=0; --ii){//from (m-1) walking backward as m is initializd in above line
                for(int ch=0; ch<26; ++ch){ //for each lowercase letter
                    next[ii][ch] = next[ii+1][ch];
                }
                next[ii][s1[ii+1]-'a']=ii+1;
            }
    
            //identify starts
            vector<int> start;
            for(int ii=1; ii<=m; ++ii) if(s1[ii]==s2[0]) start.push_back(ii);
            
            string ret = "";
            for(int ii: start){//for each start
                int jj = ii-1; //set observation index, we actually already know ii is a valid starting point
                int flag=1;
     
                for(auto ch: s2){//for each char in s2, use "next" to identify start, end index
                    jj = next[jj][ch-'a'];
                    if(jj==-1) {
                        flag=0;
                        break;
                    }
                }
                if(flag){
                    int len = jj-ii+1;
                    if(ret=="" || len < ret.size()){
                        ret = s1.substr(ii, len);
                    }
                }
              
            }
            return ret;   
        }
    };