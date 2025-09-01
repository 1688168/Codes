class Solution {
    public int minJumps(int[] arr) {
        int N = arr.length;
        if(N==1) return 0; //if only one step. no need to jump

        //create a cache to record value to index (given a value, what are the indexes we can jump to)
        Map<Integer, List<Integer>> val2idx = new HashMap<>();
        for(int ii=0; ii<N; ++ii) val2idx.computeIfAbsent(arr[ii], xx -> new ArrayList<>()).add(ii);

        //declare/define a queue (bfs)
        Queue<Integer> qq = new ArrayDeque<>();//holding nodes we can reach in this jump

        //declare/define visited to record visited nodes for pruning
        Set<Integer> visited = new HashSet<>();

        //initialize queue with first node
        visited.add(0);
        qq.offer(0);

        //perform BFS
        int level = 0;
        while(!qq.isEmpty()){
            level+=1;//we already check when N=1 (no jump)
            int sz = qq.size();
            for(int ii=0; ii<sz; ++ii){//consume all nodes in this level
                var curr_idx = qq.poll();

                //prev
                var prev_idx = curr_idx-1;
                if(prev_idx >= 0 && !visited.contains(prev_idx)){
                    visited.add(prev_idx);
                    qq.offer(prev_idx);
                }

                //next
                var next_idx = curr_idx+1;
                if(next_idx < N && !visited.contains(next_idx)){
                    visited.add(next_idx);
                    qq.offer(next_idx);
                }
                //by value
                if(val2idx.containsKey(arr[curr_idx])){
                    for(var xx: val2idx.get(arr[curr_idx])){
                        if(visited.contains(xx)) continue;
                        visited.add(xx);
                        qq.offer(xx);
                    }
                    val2idx.remove(arr[curr_idx]); //already visited all reachible nodes. prune to avoid unnecessary loop
                }
            }
            if(visited.contains(N-1)) return level;
        }
        return -1;
    }
}

// * N=10^4
// * NN=5N
// * 5NLogN = 5*10^6
// * we cannot use DP -> if we later reach an index with same value we can jump backward, that would change the prev optimal solution
// * min jump -> shortest distance -> BFS