/*
// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    static bool cmp(pair<int, int> &a, pair<int, int> &b){
        if(a.first != b.first)
            return a.first < b.first;
        else
            return a.second > b.second;
    }
public:

    vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {

        vector<pair<int, int>> events; //{time, incremental}
        for(int ii=0; ii<schedule.size(); ++ii){//for each employee's schedule
            for(auto range: schedule[ii]){//each employee has multiple ranges
                events.push_back({range.start, +1});
                events.push_back({range.end, -1});
            }
        }
        sort(events.begin(), events.end(), cmp);
        int count = 0;
        int start=-1, end=-1;
        vector<Interval> ret;
        for(auto event: events){
            count += event.second;
            if(event.second==-1 && count == 0){
                start = event.first;
            }else if(event.second==1 && count ==1 && start != -1){
                end = event.first;
                ret.push_back({start, end});
            }
        }

        return ret;
    }
};