using namespace std;

#include <iostream>
#include <vector>

class SubsetSum {
 public:
  virtual bool canPartition(const vector<int> &num, int sum) {
    vector<vector<bool>> dp(num.size(), vector<bool>(sum+1, false));
    for(int ii = 0; ii < num.size(); ++ii){
      dp[ii][0]=true;
    }
    for(int ii = 1; ii <= sum; ++ii){
      if(ii == num[0]) dp[0][ii]=true;
    }
    for(int ii = 1; ii < num.size(); ++ii){
      for(int jj=1; jj <= sum; ++jj){
        dp[ii][jj]=dp[ii-1][jj] || ((jj >= num[ii])?dp[ii-1][jj-num[ii]]:false);
      }
    }
    return dp[num.size()-1][sum];
  }
};

int main(int argc, char *argv[]) {
  SubsetSum ss;
  vector<int> num = {1, 2, 3, 7};
  cout << ss.canPartition(num, 6) << endl;
  num = vector<int>{1, 2, 7, 1, 5};
  cout << ss.canPartition(num, 10) << endl;
  num = vector<int>{1, 3, 4, 8};
  cout << ss.canPartition(num, 6) << endl;
}
