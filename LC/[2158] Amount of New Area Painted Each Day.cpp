class Solution {
public:
    vector<int> amountPainted(vector<vector<int>>& paint) {

        //given a position, collect all events with event day: {eventDay, event}
        map<int, vector<pair<int, int>>> Map; //pos->{{idx, flag}}
        //given an location, which days paints it?
        for(int ii=0; ii<paint.size(); ++ii){//Map collects all events given an position/location
            Map[paint[ii][0]].push_back({ii, 1});
            Map[paint[ii][1]].push_back({ii, -1});
        }


        //array: all sorted locations with paint event on some day 
        //events array: expands events sorted by position, position/location, each position, we have all events with date info
        vector<pair<int, vector<pair<int, int>>>> array(Map.begin(), Map.end());//cpp, expand map key/val to a vector
        set<int> Set;//to collect all paint events on some day and sorted by day. the min day is the effective paint
        vector<int> ret(paint.size());//return space (amount of new area painted on a day ii)

        for(int ii=0; ii<array.size(); ++ii){//for each position/location with event happened
            int pos = array[ii].first; //the position of this event
            for(auto& [idx, flag]: array[ii].second){//all event day/event at this position/location
                if(flag==1)
                    Set.insert(idx);//this set is sorted by day, the first date is the effective paint day
                else
                    Set.erase(idx);
            }
            if(!Set.empty())//Set not empty meaning the location is painted by multiple days, and the first day is the effective paint
                //until the next event, all painting belong to this day. we will evalute on next event point see which day contributed the painting
                ret[*Set.begin()] += array[ii+1].first - array[ii].first;//array is loc, (day, flag)
        }
        return ret;
    }
};