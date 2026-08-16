class Solution {
public:
    string decodeString(string s) {
        stack<string> str;
        stack<int> nums;
        string curr;
        for(int ii=0; ii<s.size(); ++ii){
            if(isdigit(s[ii])){
                int i0=ii;
                while(ii<s.size() && isdigit(s[ii])) ++ii;

                int num = stoi(s.substr(i0, ii-i0));
                str.push(curr);
                nums.push(num);
                curr="";
            }else if(s[ii]==']'){
                int num = nums.top();
                string temp = curr;
                for(int jj=0; jj<num-1; ++jj) curr += temp;
                nums.pop();
                curr = str.top()+curr;
                str.pop();
            }else{
                curr.push_back(s[ii]);
            }
        }

        return curr;
    }
};