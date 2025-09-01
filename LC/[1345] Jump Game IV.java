
class Solution {
    public int minJumps(int[] arr) {
        int N = arr.length;
        if(N==1) return 0;

        //val2idx (cache given a val -> lookup all indexes with this value)
        Map<Integer, List<Integer>> val2idx= new HashMap<>();
        for(int ii=0; ii<N; ++ii)
            val2idx.computeIfAbsent(arr[ii], kk -> new ArrayList<>()).add(ii); //[java][hashmap][computeIfAbsent][create if not existing]
        
        boolean[] visited = new boolean[N];
        
        //deque for queue
        Deque<Integer> q = new ArrayDeque<>(); 

        //root node
        q.offer(0);
        visited[0] = true;
        int level=0;

        while(!q.isEmpty()){//[java][isempty][check q empty]
            int sz = q.size();//BFS level by level traverse
            for(int zz=0; zz<sz; ++zz){//for each elements in this level
                var curr = q.poll();//curr_idx
                var prev=curr-1;
                var nxt = curr+1;

                if(nxt < N && !visited[nxt]){
                    visited[nxt]=true;
                    q.offer(nxt);

                }
                
                if(prev >= 0 && !visited[prev]){
                    visited[prev]=true;
                    q.offer(prev);
          
                }
                
                if(val2idx.containsKey(arr[curr])){
                    for(var nn: val2idx.get(arr[curr])){
                        if(!visited[nn]){
                            q.add(nn);
                            visited[nn]=true;
                        }
                    }
                    val2idx.remove(arr[curr]); //if the whole value is visited, no need to check again.
                }
            }
            level+=1;
            if(visited[N-1]) return level;
          
        }
        return -1;
    }
}