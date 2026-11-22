class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        vector<pair<int, int>> tasks;
        for(int ii=0; ii<profits.size(); ++ii){
            tasks.push_back({capital[ii], profits[ii]});
        }
        sort(tasks.begin(), tasks.end());

        priority_queue<int> pq;
        int count=0;
        int ii=0;
        while(count < k){
            while(ii<tasks.size() && tasks[ii].first <= w){
                pq.push(tasks[ii].second);
                ++ii;
            }
            if(pq.empty()) break;
            w += pq.top();
            pq.pop();
            ++count;
        }
        return w;
    }
};