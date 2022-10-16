using namespace std;

#include <iostream>
#include <vector>

class MissingNumber {
 public:
  static int findMissingNumber(vector<int> &nums) {
    int ii=0;
    while(ii < nums.size()){
      if(nums[ii] < nums.size() && nums[ii] != ii){
        swap(nums[ii], nums[nums[ii]]);
        continue;
      }
      ++ii;
    }

    ii=0;
    while(ii < nums.size()){
      if(nums[ii] != ii)break;
      ++ii;
    }

    return ii;
  }
};
