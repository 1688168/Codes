class Solution {
    public String minWindow(String s1, String s2) {
        //take s1,s2 metrics
        int N1=s1.length();
        int N2=s2.length();

        //insert dummy
        s1="#"+s1;
        s2="#"+s2;

        //declare finite-state-machine
        var next = new int[N1+1][26];

        //initialize next
        //what's the know initial state -> no next @ end of s1
        for(int ch=0; ch<26;++ch) next[N1][ch]=-1;//-1 indicate no next
        //build all states from initial state
        for(int ii=N1-1; ii>=0; --ii){//ii=N1 is covered by above line, going backward
            for(int ch=0; ch<26;++ch)
                next[ii][ch]=next[ii+1][ch];//check out of bound on ii+1
            next[ii][s1.charAt(ii+1)-'a'] = ii+1;//s1[ii]'s next idx of s1[ii+1] is ii+1
        }
        
        //collect all starts
        var starts = new ArrayList<Integer>();
        for(int ii=1; ii<=N1; ++ii) if(s1.charAt(ii)==s2.charAt(1)) starts.add(ii);
        
        //for each start find the substring and maintain the shortest one
  
        String res="";
        int len = Integer.MAX_VALUE;
        for(var st: starts){
            Boolean flag = true;//assuming we could find the subsequence from this st
            var ed = st;//end index from s1
            for(int jj=2; jj<=N2; ++jj){//jj is index into s2
                ed=next[ed][s2.charAt(jj)-'a'];//find subsequence from s2
                //System.out.println("st: " + st + " ed: " + ed);
                if(ed==-1){//can we find all index in s1 that covers s2?
                    flag=false;
                    break;
                }
            }
            //System.out.println(" out of loop: ed: " + ed);
            if(flag && (ed-st+1) < len) {//if we have a qualified substring and shorter
                res=s1.substring(st, ed+1);
                len=ed-st+1;
            }
        }
        return res;        
    }
}
/*
Problem statements:
1. find min substring from s1 s.t. s2 is a subsequence

Analysis:
* two series -> DPIII: M*N
* Bruteforce: 
  for each start, two pointers/greedy to find shortest substring of S1 s.t. s2 is a subsequence.  S*m*n
* finite-state-machine:
   pre-build next[ii][ch]: the idx of ch in s1 after s[ii]
   s*(N)+26*N
*/
