class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) 
    {
        if (S==T) return 0; //special handle source is destination
        
        unordered_map<int,vector<int>>stop2bus; //what are the buses covering the stop
        for (int i=0; i<routes.size(); i++)
        {
            for (auto j: routes[i])
                stop2bus[j].push_back(i);
        }
        
        unordered_set<int>visitedStop;
        unordered_set<int>visitedBus;
        
        queue<int>q;
        q.push(S);//starting stop
        visitedStop.insert(S);
        int step = -1;
        
        while (!q.empty())//BFS stops
        {
            step += 1;
            
            int len = q.size();
            while (len--)//for all stops we can visit at this level
            {
                int curStop = q.front();
                q.pop();
                
                for (auto bus: stop2bus[curStop])//what are the buses covering this top
                {
                    if (visitedBus.find(bus)!=visitedBus.end())//filter out buses that is visited
                        continue;
                    visitedBus.insert(bus);                        
                    
                    for (auto nextStop: routes[bus])//adding all the stops that we can visit by the bus
                    {
                        if (visitedStop.find(nextStop)!=visitedStop.end())
                            continue;
                        if (nextStop==T)
                            return step+1;
                        
                        q.push(nextStop);
                        visitedStop.insert(nextStop);
                    }
                }
            }
        }
        
        return -1;
    }
};
