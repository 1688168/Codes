class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> Map; //events - {timestamp, diff}
        for(auto interval: intervals){
            Map[interval[0]] += 1;
            Map[interval[1]] -= 1;
        }

        int sum=0;
        int ret=0;
        for(auto & [ts, diff]: Map){
            sum+=diff;
            ret = max(ret,sum);
        }

        return ret;
    }
};