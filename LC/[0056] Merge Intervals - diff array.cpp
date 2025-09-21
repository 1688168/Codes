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