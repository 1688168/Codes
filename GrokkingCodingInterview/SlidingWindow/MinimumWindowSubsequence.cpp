#include <climits>

string MinWindow(string str1, string str2){
    int min_len=INT_MAX;//initialize ans
    string ans;
    int kk;
    for(int ii=0; ii<str1.size(); ++ii){
        if(str1[ii] != str2[0]) continue; //find starting position from str1 that is same as str2[0]
        int jj=ii+1;
        kk=1;
        while(jj < str1.size() && kk < str2.size()){
            if(str1[jj]==str2[kk]){
                ++jj;
                ++kk;
            }else{
                ++jj;
            }
        }
        if(kk==str2.size() && jj<= str1.size()){
            if(jj-ii < min_len){           
                min_len=jj-ii;
                ans=str1.substr(ii, min_len);
                cout << " ans: " << ans << endl;
            }
        }

    }
    return min_len==INT_MAX? "":ans;
}