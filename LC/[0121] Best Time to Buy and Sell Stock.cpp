class Solution {
public:

    int maxProfit(vector<int>& prices) {
        int min_so_far=prices[0];
        int max_p_so_far=0;

        for(int ii=0; ii<prices.size(); ++ii){
            min_so_far=min(min_so_far, prices[ii]);
            max_p_so_far=max(max_p_so_far, prices[ii]-min_so_far);
        }

        return max_p_so_far;
    }
};
