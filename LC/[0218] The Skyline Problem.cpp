class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        //sorted map to record events
        map<int, vector<pair<int, int>>> Map; //pos -> {{height, flag}}
        for(auto building: buildings){//recording all the event points
            Map[building[0]].push_back({building[2], 1});//starting event
            Map[building[1]].push_back({building[2], -1});//ending event
        }

        multiset<int> Set;//sorted multiset
        vector<vector<int>> rets;
        for(auto& [pos, pairs]:Map){//c++ unpacking map. --- for each event --- for each x --- in each position
            for(auto & [height, flag]: pairs){//unpack pair --- all the pairs in this loop are with same x --- evaluating all the heights in this x
                if(flag==1){//if this is a starting event of a height
                    Set.insert(height);//same height is allowed. set will sort the height at this x
                }else{//this is an ending event of a height, we will need to remove one from this height, but doesn't matter which one to rmeove so we remove the first one
                    Set.erase(Set.find(height));//remove the first one with this height in the multiset
                }
            }
            //after processing all heights in this position x, we want to update for the max H or ending if no more
            //so H could be 0 (no height left ---> ending) or the max H (right most point from sorted Set)
            int H = Set.empty()?0:*Set.rbegin();//for each event, what's the current max h? remember this is a sorted multiset

            //if rets is empty (we want this H regardless) otherwise filter out the H if it is same as previous H (merge same heights)
            if(rets.empty() || rets.back()[1] != H)//height is changing or we are ending
                rets.push_back({pos, H});
        }

        return rets;
    }
};

/*
* we were given the profile of all buildings.  -> output the overall profile (merge all profiles) of all the buildings.
* we only care about those turning points and only care about the max H for overlapping turning points
* typically in diff array, we need to accumulate events, but in this case, we keep the max events
*/