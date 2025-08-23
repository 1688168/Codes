class Solution {
public:
    int minJumps(vector<int>& arr) {
        int N = arr.size();
        if(N==1) return 0; //if only 1 element -> no step required to reach end
        unordered_map<int, vector<int>> val2idx; //given a value, all index on the array with that value
        for(int ii=0; ii<N; ++ii) val2idx[arr[ii]].push_back(ii); //populate the map
        vector<int> visited(N, 0);//recording visited nodes
        queue<int> q; //for BFS
        q.push(0);//initially @ idx=0
        visited[0]=1;
        
        int level = 0;
        while(!q.empty()){//for each level
            auto sz = q.size();
            while(sz--){ //all elements in this level
                auto curr_idx = q.front();
                q.pop();
                //add all next level canbdidates to the queue and mark visited
                // case I: ii+1
                if(curr_idx+1 < N && visited[curr_idx+1]==0){
                    q.push(curr_idx+1);
                    visited[curr_idx+1]=1;
                } 
                
                // case II: ii-1
                if(curr_idx-1 >= 0 && visited[curr_idx-1]==0){
                    q.push(curr_idx-1);
                    visited[curr_idx-1]=1;
                }
                // case III: all elements with same value
                for(auto next: val2idx[arr[curr_idx]]){//notice this loop inside loop -> N^2 -> try to prune this
                    if(visited[next] == 0){
                        q.push(next);
                        visited[next]=1;
                    }
                }    
                val2idx.erase(arr[curr_idx]);//prune
            }
            ++level; 

            //all indexes with this value can be pruned as they were all visited in this level -> avoid the N*N nested loop
            if(visited[N-1]==1) return level; //if last idx is added to visited in curr_idx (it's actually the next level)
    
        }

        return level;
    }
};