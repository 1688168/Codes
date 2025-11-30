class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        unordered_map<int, int> Map;
        for(int ii=0; ii<flowers.size(); ++ii){
            int s = flowers[ii][0], e=flowers[ii][1];
            Map[s] += 1;
            Map[e+1] -= 1;
        }
        //c++ converting Map to vector of pair
        vector<pair<int, int>> diff(Map.begin(), Map.end());
        sort(diff.begin(), diff.end());

        vector<pair<int, int>> p;
        for(int ii=0; ii<people.size(); ++ii){
            p.push_back({people[ii], ii});
        }
        sort(p.begin(), p.end());

        int jj = 0;
        int sum=0;
        vector<int> rets(people.size());
        for(int ii=0; ii<p.size(); ++ii){
            while(jj<diff.size() && diff[jj].first <= p[ii].first){
                sum += diff[jj].second;
                ++jj;
            }
            rets[p[ii].second]=sum;

        }

        return rets;
        

        
    }
};

// ### given
// * flowers[ii] = [starti, endi] -- interval (inclusive)
// * people[ii] = the time iith person will arrive

// ### ask
// * answer[ii] = num of flowers in full bloom when the iith person arrives

// ### analysis
// * N=5*10^4 -- num of intervals
// * interval addition -> sweepline

// ### strategy
// * convert to event - N
// * sort events = nlogn
// * aggregate events = N
// * output answer
