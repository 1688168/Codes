// 20240823
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int N = strs.size();
        auto dp = vector<vector<int>>(m+1, vector<int>(n+1, 0));

        for(int ii=0; ii<N; ++ii){
            int zz=0;
            int oo=0;
            //count zero/ones
            for(auto x: strs[ii]){
                if(x=='0'){
                    ++zz;
                }else{
                    ++oo;
                }       
            }

            auto tmp = dp;
            for(int jj=zz; jj<=m; ++jj){
                for(int kk=oo; kk<=n; ++kk){
                    dp[jj][kk] = max(tmp[jj][kk], tmp[jj-zz][kk-oo]+1);
                }
            }
        }
        return dp[m][n];
    }
};

//=========================
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) 
    {
        auto dp=vector<vector<int>>(m+1,vector<int>(n+1, 0));
        
        for (int k=0; k<strs.size(); k++) //for each resource
        {
            int ones=0; //count zero and ones
            int zeros=0;
            for (int i=0; i<strs[k].size(); i++)
            {
                if (strs[k][i]=='0') zeros++;
                else ones++;
            }
                            
            auto temp=dp;
            for (int i=zeros; i<=m; i++)
                for (int j=ones; j<=n; j++)
                {
                    dp[i][j]=max(temp[i][j],temp[i-zeros][j-ones]+1);
                }
        }
                
        return dp[m][n];
    }
};