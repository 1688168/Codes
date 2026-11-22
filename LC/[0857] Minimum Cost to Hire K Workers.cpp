class Solution {
    static bool cmp(pair<int, int> &a, pair<int, int>&b){
        return a.second*1.0/a.first < b.second*1.0/b.first;
    }
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<int, int>> persons;
        for(int ii=0; ii<quality.size(); ++ii){
            persons.push_back({quality[ii], wage[ii]});
        }
        sort(persons.begin(), persons.end(), cmp);

        int quality_sum=0;
        priority_queue<int> pq;
        double ret = 1e20;
        for(int ii=0; ii<persons.size(); ++ii){
            double unitWage = persons[ii].second*1.0/persons[ii].first;
            quality_sum += persons[ii].first;
            while(pq.size()>k-1){
                quality_sum -= pq.top();
                pq.pop();
            }

            if(pq.size()==k-1)
                ret = min(ret, unitWage*quality_sum);
            pq.push(persons[ii].first);
        }

        return ret;
    }
};