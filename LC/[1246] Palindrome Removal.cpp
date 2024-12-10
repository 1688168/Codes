class Solution {
public:
    int minimumMoves(vector<int>& arr) 
    {
        int N = arr.size(); 
        arr.insert(arr.begin(),0);
        
        auto dp = vector<vector<int>>(N+2,vector<int>(N+2,0));        
      
        for (int len = 1; len <= N; len++)   //for each substring len        
            for (int i = 1; i+len-1<=N; i++) //for each starting idx
            { 
                int j = i+len-1;//the ending idx
                dp[i][j] = INT_MAX/2; //default to inf               
                for (int k=i; k<=j; k++) //for each partition in the range
                {
                    if (arr[k]==arr[j])
                        dp[i][j] = min(dp[i][j], dp[i][k-1]+max(1,dp[k+1][j-1]));
                } 
            }         
  
        return dp[1][N]; 
    }
};