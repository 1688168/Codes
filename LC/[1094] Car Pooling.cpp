class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<pair<int,int>> events;
        for(auto trip: trips){
            events.push_back({trip[1], +trip[0]});
            events.push_back({trip[2], -trip[0]});
        }
        sort(events.begin(), events.end());

        int total=0;
        for(auto event: events){
            total += event.second;
            if(total > capacity) return false;
        }
        return true;
    }
};