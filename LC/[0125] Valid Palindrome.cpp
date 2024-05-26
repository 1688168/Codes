class Solution {
public:
    bool isPalindrome(string s) {
        int N = s.size();
        int ll=0, rr=N-1;

        while (ll<rr){
            while(ll<rr && !isalnum(s[ll])) ++ll;
            while(rr>ll && !isalnum(s[rr])) --rr;

            if(tolower(s[ll]) != tolower(s[rr])) return false;
            ++ll;
            --rr;
        }        
        return true;
    }
};