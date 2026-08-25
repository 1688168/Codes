class Solution {
public:
    string crackSafe(int n, int k) {
        unordered_map<string, int> Map;
        string ans;
        for(int ii=0; ii<n-1; ++ii) ans += '0';
        for(int ii=0; ii<pow(k, n); ++ii){
            string key = ans.substr(ans.size()-(n-1), n-1);//takes the last n digits
            Map[key] = (Map[key]+1)%k;
            ans.push_back('0'+Map[key]);
        }
        return ans;
    }
};


/*


## Problem Statement 
* given: k (0...k) and n (num of digits of the passcode)
* ask: what's the shortest string that guarantees we can open the safe.  (last n digits count)

## Analysis:
* "De Bruijin Series"

*/