using LL = long long;
class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) 
    {
        LL left = 0,  right = LLONG_MAX; //max long constance
        while (left < right) //template for binary search
        {
            LL mid = right-(right-left)/2;
            if (isOK(stations, r, k, mid))
                left = mid;
            else
                right = mid-1;
        }
        return left;
    }
    
    bool isOK(vector<int>stations, int r, LL k, LL m)
    {
        int n = stations.size();
        LL sum = 0; //can we make all station with power greater than k?
        
        //initial righ wing in ranges, avoid out of bound check
        for (int i=0; i<=min(n-1, r-1); i++) 
            sum += stations[i];
            
        for (int i=0; i<n; i++)//check for each station required power
        {
            if (i+r < n)            
                sum += stations[i+r];            
                
            if (i-r-1 >= 0)
                sum -= stations[i-r-1];
                        
            if (sum >= m) continue; //pass
            
            LL diff = m - sum; 
            if (diff > k) 
                return false;
            stations[min(n-1, i+r)] += diff; //ensure we are not modifying the original
            sum = m;
            k -= diff;
        }
        return true;
    }
};