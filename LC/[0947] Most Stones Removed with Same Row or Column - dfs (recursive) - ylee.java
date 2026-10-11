class Solution {

    private boolean is_connected(int[][]stones, int aa, int bb){
        return (stones[aa][0] == stones[bb][0]) || (stones[aa][1] == stones[bb][1]);
    }

    private void dfs(int idx, Set<Integer> visited, int[][] stones){
        int N = stones.length;
        //from this stone, we need to explore (DFS) all connected stones
        for(int ii=0; ii<N; ++ii){
            if(idx==ii) continue; //skip self
            if(!visited.contains(ii) && is_connected(stones, idx, ii)) 
            {
                visited.add(ii);
                dfs(ii, visited, stones);
            }
        }
    }        
    public int removeStones(int[][] stones) {
        int N = stones.length;
        //we want to DFS on all stones and identify how many disconnected groups

        Set<Integer> visited = new HashSet<>();
        //try each stone and skip visited
        int cnt = 0;
        for(int ii=0; ii<N; ++ii){
            if(visited.contains(ii)) continue;
            ++cnt; //a new disconnected group
            visited.add(ii);
            dfs(ii, visited, stones);
        }

        return N-cnt;
    }
}