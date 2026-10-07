class Solution {
    private void dfs(int node, Set<Integer> visited, int[][] isConnected){
        for(int ii=0; ii<isConnected.length; ++ii){
            if(isConnected[node][ii]==1 && !visited.contains(ii)){
                visited.add(ii);
                dfs(ii, visited, isConnected);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        Set<Integer> visited = new HashSet<>();
        int N = isConnected.length;
        int cnt=0;
        for(int ii=0; ii<N; ++ii){
            if(!visited.contains(ii)){
                ++cnt;
                visited.add(ii);
                dfs(ii, visited, isConnected);
            }
        }
        return cnt;
    }
}