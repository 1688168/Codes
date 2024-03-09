class Solution {
    int n;
public:
    int maxProfit(int k, vector<int>& prices) {
        n = prices.size();
        prices.insert(prices.begin(), 0);

        int left=0, right = *max_element(prices.begin(), prices.end());
        while(left < right){
            int fee=left+(right-left)/2;
            if (maxProfitWithFee(prices, fee)[1] > k){
                left = fee+1;
            }else{
                right = fee;
            }
        }

        return maxProfitWithFee(prices, left)[0]+left*k;

    }

    vector<int> maxProfitWithFee(vector<int> & prices, int fee){
        vector<int> hold(n+1, 0);//bought
        vector<int> sold(n+1, 0);//sold
        sold[0]=0;
        hold[0]=INT_MIN/2;
        int count_sold=0, count_hold=0;

        for(int ii=1; ii<=n; ++ii){
            if(sold[ii-1] >= hold[ii-1]+prices[ii]){
                sold[ii]=sold[ii-1];
            }else{
                sold[ii]=hold[ii-1]+prices[ii];
                count_sold = count_hold;
            }

            if(hold[ii-1] >= sold[ii-1]-prices[ii]-fee){
                hold[ii]=hold[ii-1];
            }else{
                hold[ii]=sold[ii-1]-prices[ii]-fee;
                count_hold= count_sold+1;
            }
        }

        return {sold[n], count_sold};

    }
};