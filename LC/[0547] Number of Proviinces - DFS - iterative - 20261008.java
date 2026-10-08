class Solution {
    public int findCircleNum(int[][] isConnected) {
        int N=isConnected.length; //num of cities

        //we need to dfs all cities and count connected groups
        Set<Integer> visited = new HashSet<>();
        Deque<int[]> stack = new ArrayDeque<>();
        int cnt=0;
        for(int ii=0; ii<N; ++ii){
            if(visited.contains(ii)) continue;
            visited.add(ii);
            stack.push(new int[]{ii, 0});
            ++cnt;
            while(!stack.isEmpty()){
                var frame = stack.peek();
                int curr = frame[0];
                int connected_idx = frame[1];
                ++frame[1];
                if(connected_idx==N){
                    stack.pop();
                    continue;
                }

                if(!visited.contains(connected_idx) && isConnected[curr][connected_idx]==1){
                    visited.add(connected_idx);
                    stack.push(new int[]{connected_idx, 0});
                }
            }
        }
        return cnt;
    }
}