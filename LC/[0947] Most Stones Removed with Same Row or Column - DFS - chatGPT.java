import java.util.*;

class Solution {
    /*
     * Each stone is a graph node.
     * Two stones are connected if they share a row or column.
     * For each connected component, keep one root stone and remove all others.
     * Use DFS postorder so children are removed before parents.
     */
    public List<int[]> removeStonesSequence(int[][] stones) {
        int n = stones.length; //java take array length

        Map<Integer, List<Integer>> rowMap = new HashMap<>(); //java hashmap to k/v lookup
        Map<Integer, List<Integer>> colMap = new HashMap<>();

        // Use each stone's index as its graph node id.
        for (int i = 0; i < n; i++) {
            int x = stones[i][0];
            int y = stones[i][1];

            //populate the row/col look up hashmap
            rowMap.computeIfAbsent(x, k -> new ArrayList<>()).add(i); //java insert/create to hashmap
            colMap.computeIfAbsent(y, k -> new ArrayList<>()).add(i);
        }

        // Graph representation as an adjacency list.
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Connect stones sharing the same row.
        for (List<Integer> indices : rowMap.values()) {
            connectGroup(indices, graph);
        }

        // Connect stones sharing the same column.
        for (List<Integer> indices : colMap.values()) {
            connectGroup(indices, graph);
        }

        boolean[] visited = new boolean[n];
        List<Integer> removalOrder = new ArrayList<>();

        // Run DFS for each connected component.
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, true, graph, visited, removalOrder);
            }
        }

        // Convert stone indices back to coordinates.
        List<int[]> result = new ArrayList<>();

        for (int idx : removalOrder) {
            result.add(stones[idx]);
        }

        return result;
    }

    private void connectGroup(List<Integer> indices, List<List<Integer>> graph) {
        if (indices.size() <= 1) {
            return;
        }

        int first = indices.get(0);

        for (int i = 1; i < indices.size(); i++) {
            int other = indices.get(i);

            graph.get(first).add(other);
            graph.get(other).add(first);
        }
    }

    private void dfs(
        int node,
        boolean isRoot,
        List<List<Integer>> graph,
        boolean[] visited,
        List<Integer> removalOrder
    ) {
        visited[node] = true;

        for (int nei : graph.get(node)) {
            if (!visited[nei]) {
                dfs(nei, false, graph, visited, removalOrder);
            }
        }

        // Postorder: remove this stone only after its DFS children are processed.
        // Do not remove the root stone of this component.
        if (!isRoot) {
            removalOrder.add(node);
        }
    }
}