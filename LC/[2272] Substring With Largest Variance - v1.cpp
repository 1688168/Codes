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
