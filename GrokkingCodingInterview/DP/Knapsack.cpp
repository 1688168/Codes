using namespace std;

#include <iostream>
#include <vector>

class Knapsack {
 public:
  int solveKnapsack(const vector<int> &profits, vector<int> &weights, int capacity) {
    vector<int> dp(capacity+1, -1);
    //initialize row 0
    for(int =0; ii<=capacity; ++ii){
      ii >= weights[ii]?dp[ii]=profits[ii]:0;
    }

    for(int ii=1; ii<weights.size(); ++ii){
      for(int jj=capacity; jj >=0; --jj){
        if(jj >= weights[ii])
          dp[jj]=max(dp[jj], dp[jj-weights[ii]]+profits[ii]);

      }
    }

    return dp[capacity];
  }
};

int main(int argc, char *argv[]) {
  Knapsack ks;
  vector<int> profits = {1, 6, 10, 16};
  vector<int> weights = {1, 2, 3, 5};
  int maxProfit = ks.solveKnapsack(profits, weights, 6);
  cout << "Total knapsack profit ---> " << maxProfit << endl;
  maxProfit = ks.solveKnapsack(profits, weights, 7);
  cout << "Total knapsack profit ---> " << maxProfit << endl;
}
