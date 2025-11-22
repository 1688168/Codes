class Solution {
public:
    vector<vector<long long>> splitPainting(vector<vector<int>>& segments) {
        map<long long, long long> events;
        for(auto seg: segments){
            events[seg[0]] += seg[2];
            events[seg[1]] -= seg[2];
        }

        vector<vector<long long>> rets;
        long long cnt = 0;
        long long start = -1, end = -1;
        for(auto const & [pos, diff]: events){

            if(start == -1){
                start = pos;
            }else{
                end = pos;
                rets.push_back({start, end, cnt});
                start = end;
            }
            cnt += diff;

            if(cnt==0) start = -1;
        }
        return rets;
    }
};