/*
* 20240225
*/
/*
    => largest variance for all substring in S
    * for all char pairs (a, b) --- Time 26*26
    * let a=1, b=-1, others=0 and calc max subarray sum
    * max subarray sum -> modified Kadane (since need two chars)
    => Overall Time: 26*26*N
*/

class Solution {
public:
    int largestVariance(string s) {
        int n = s.size();//take size of the string
        unordered_set<char> Set(s.begin(), s.end()); //add all chars in the string to set
        int ret = 0;
        for(char a: Set)
            for(char b: Set){//26*26 combinations
                if(a==b) continue; //need two chars
                /* Type I DP: best use tmp var to avoid two vars interfering each other.  here the order matters and avoids the interferring
                */
                int dp0=0, dp1=INT_MIN/2; 
                //now we have a pair of chars (a, b)
                //(modified) kadane to find the max subarray sum
                for(int ii=0; ii<n; ++ii){
                    if(s[ii]==a){
                        dp1 = dp1+1;
                        dp0 = dp0 + 1; 
                    }else if(s[ii]==b){ //here is else if as others are 0
                        dp1 = max(dp0-1, dp1-1);
                        dp0=0;
                    }
                    ret = max(ret, dp1);
                }
            }
          
        return ret;
    }
   
};


/* ------------ */
class Solution {
public:
    int largestVariance(string s)
    {
        int n = s.size();
        unordered_set<char>Set(s.begin(), s.end()); //remove duplicates

        int ret = 0;

        for (auto a: Set) //try all pairs (we need max/min freq for variance)
            for (auto b: Set)
            {
                if (a==b) continue;//skip same letters as var=0
                //curSum0: the max subarray sum ending at ii, and this subarray does NOT contain -1
                //curSum1: the max subarray sum ending at ii, and this subarray does contain -1
                int curSum0 = 0,  curSum1 = INT_MIN/2;

                for (int i=0; i<n; i++)//running sum for each ii
                {
                    if (s[i] == a)//ending @ a, both length increase
                    {
                        curSum0 = curSum0 + 1;
                        curSum1 = curSum1 + 1;
                    }
                    else if (s[i] == b)//update global max when we have b
                    {
                        //curSum0 never seen b now we have b
                        //currSum1 already has b, so we need to ignore the curr b
                        curSum1 = max(curSum0-1, curSum1-1);
                        curSum0 = 0;
                    }

                    ret = max(ret, curSum1);
                }
            }

        return ret;
    }
};
