class Solution {
    static bool cmp(pair<int, int> &a, pair<int, int>&b){
        if(a.first != b.first)
            return a.first < b.first;
        else
            //opening interval need to go first
            //recall the use case 
            /*
                [.   ]
                     [.    ]
                     ^ we need to do +1 first or this will create two interval if we do -1 first.
            */
            return b.second < a.second;//
    }
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<pair<int, int>> diff; //{timeStamp}
        for(auto &interval: intervals){
            diff.push_back({interval[0], +1});
            diff.push_back({interval[1], -1});
        }
        sort(diff.begin(), diff.end(), cmp);

        int sum=0;
        int start, end;
        vector<vector<int>> ret;
        for(int ii=0; ii<diff.size(); ++ii){
            if(sum==0 && diff[ii].second==1){//a start
                start = diff[ii].first;
            }else if (sum > 0 && sum + diff[ii].second==0){
                end = diff[ii].first;
                ret.push_back({start, end});
            }
            sum += diff[ii].second;
        }
        return ret;
    }
};

// optimized by chatGPT
#include <bits/stdc++.h>
using namespace std;

class Solution {
    // Event: (+1) = open, (-1) = close
    // Sort by time asc; at same time: OPEN before CLOSE to merge touching/closed intervals.
    static bool cmp(const pair<long long,int>& a, const pair<long long,int>& b) {
        if (a.first != b.first) return a.first < b.first;
        // want (+1) before (-1) when times tie
        return a.second > b.second; // +1 (open) > -1 (close)
    }

public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};

        vector<pair<long long,int>> diff;
        diff.reserve(intervals.size() * 2);

        for (const auto& it : intervals) {
            long long l = it[0], r = it[1];
            diff.emplace_back(l, +1);
            diff.emplace_back(r, -1);
        }

        sort(diff.begin(), diff.end(), cmp);

        long long sum = 0;
        long long start_ts = 0;
        vector<vector<int>> res;
        res.reserve(intervals.size());

        for (const auto& e : diff) {
            const long long t = e.first;
            const int delta = e.second;

            // if we are currently outside any interval and see an OPEN, this is a new start
            if (sum == 0 && delta == +1) {
                start_ts = t;
            }
            // if we are inside and this event will bring coverage to zero, we end at t
            else if (sum > 0 && sum + delta == 0) {
                long long end_ts = t;
                // cast back to int if you’re sure input fits in int
                res.push_back({static_cast<int>(start_ts), static_cast<int>(end_ts)});
            }

            sum += delta;
        }

        return res;
    }
};