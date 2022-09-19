class Solution {
public:
    int maxEvents(vector<vector<int>>& events)
    {
        //greedy: sort by start time and end time.
        //attend the one started first.
        //evict all expired the next day and attend the one ends first
        sort(events.begin(), events.end());
        priority_queue<int, vector<int>, greater<int>>pq;
        int i = 0;
        int ret = 0;
        for (int day=1; day<=100000; day++)//each day see who got in scope
        {
            while (i<events.size() && events[i][0]<=day)//if you happen today, add to pq
            {
                pq.push(events[i][1]);
                i++;
            }
            while (!pq.empty() && pq.top() < day)//evict all those expired
                pq.pop();
            if (!pq.empty())
            {
                pq.pop();//take the one ends first and add count
                ret++;
            }
        }
        return ret;
    }
};
