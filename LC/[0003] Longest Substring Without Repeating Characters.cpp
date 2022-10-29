class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> char2loc;

        int ll=0, rr=0;
        int mxl=0;
        for(rr=0; rr<s.size(); ++rr){
            char cc=s[rr];

            if(char2loc.find(cc) != char2loc.end()){
                ll=max(ll, char2loc[cc]+1);
            }
            char2loc[cc]=rr;
            mxl=max(mxl, rr-ll+1);

        }

        return mxl;

    }
};
