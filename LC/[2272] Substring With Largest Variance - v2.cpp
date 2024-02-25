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
        unordered_map<char, vector<int>>Map;
        for(int ii=0; ii<n; ++ii){//take all index location of each chars
            Map[s[ii]].push_back(ii);
        }
        //unordered_set<char> Set(s.begin(), s.end()); //add all chars in the string to set
        int ret = 0;
        for(auto & [a, pos0]: Map)
            for(auto & [b, pos1]: Map){//26*26 combinations
                if(a==b) continue; //need two chars
                /* Type I DP: best use tmp var to avoid two vars interfering each other.  here the order matters and avoids the interferring
                */
                int dp0=0, dp1=INT_MIN/2; 
                //now we have a pair of chars (a, b)
                //(modified) kadane to find the max subarray sum

                int ii=0, jj=0;

                while(ii < pos0.size() || jj < pos1.size()){
                    if(jj==pos1.size() || (ii<pos0.size() &&pos0[ii]<pos1[jj])){//whoever is in the front is 1, 
                        dp1 = dp1+1;
                        dp0 = dp0 + 1; 
                        ++ii;
                    }else if(ii==pos0.size() || (jj < pos1.size() && pos1[jj] < pos0[ii])){ //here is else if as others are 0
                        dp1 = max(dp0-1, dp1-1);
                        dp0=0;
                        ++jj;
                    }
                    ret = max(ret, dp1);
                }
            }
          
        return ret;
    }
   
};

/* --------------- */
class Solution {
public:
    int largestVariance(string s)
    {
        int n = s.size();
        unordered_map<char, vector<int>>Map;
        for (int i=0; i<n; i++)
            Map[s[i]].push_back(i);

        int ret = 0;

        for (auto& [a, pos0]: Map)
            for (auto& [b, pos1]: Map)
            {
                if (a==b) continue;
                int curSum0 = 0,  curSum1 = INT_MIN/2;

                int i = 0, j = 0;

                while (i<pos0.size() || j<pos1.size())
                {
                    if (j==pos1.size() || (i<pos0.size() && pos0[i] < pos1[j]))
                    {
                        curSum0 = curSum0 + 1;
                        curSum1 = curSum1 + 1;
                        i++;
                    }
                    else if (i==pos0.size() || (j<pos1.size() && pos1[j] < pos0[i]))
                    {
                        curSum1 = max(curSum0-1, curSum1-1);
                        curSum0 = 0;
                        j++;
                    }

                    ret = max(ret, curSum1);
                }
            }

        return ret;
    }
};
