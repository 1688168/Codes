#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    /*
     * Each stone is a graph node.
     * Two stones are connected if they share a row or column.
     * For each connected component, keep one root stone and remove all others.
     * Use DFS postorder so children are removed before parents.
     */
    vector<vector<int>> removeStonesSequence(vector<vector<int>>& stones) {
        int n = stones.size();

        unordered_map<int, vector<int>> rowMap;
        unordered_map<int, vector<int>> colMap;

        // Use each stone's index as its graph node id.
        for (int i = 0; i < n; i++) {
            int x = stones[i][0];
            int y = stones[i][1];

            rowMap[x].push_back(i);
            colMap[y].push_back(i);
        }

        // Graph representation as an adjacency list.
        vector<vector<int>> graph(n);

        // Connect stones sharing the same row.
        for (auto& [row, indices] : rowMap) {
            connectGroup(indices, graph);
        }

        // Connect stones sharing the same column.
        for (auto& [col, indices] : colMap) {
            connectGroup(indices, graph);
        }

        vector<bool> visited(n, false);
        vector<int> removalOrder;

        // Run DFS for each connected component.
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, true, graph, visited, removalOrder);
            }
        }

        // Convert stone indices back to coordinates.
        vector<vector<int>> result;
        for (int idx : removalOrder) {
            result.push_back(stones[idx]);
        }

        return result;
    }

private:
    void connectGroup(vector<int>& indices, vector<vector<int>>& graph) {
        if (indices.size() <= 1) {
            return;
        }

        int first = indices[0];

        for (int i = 1; i < indices.size(); i++) {
            int other = indices[i];

            // Add undirected edge: first <-> other.
            graph[first].push_back(other);
            graph[other].push_back(first);
        }
    }

    void dfs(
        int node,
        bool isRoot,
        vector<vector<int>>& graph,
        vector<bool>& visited,
        vector<int>& removalOrder
    ) {
        visited[node] = true;

        // Visit children/neighbors first.
        for (int nei : graph[node]) {
            if (!visited[nei]) {
                dfs(nei, false, graph, visited, removalOrder);
            }
        }

        // Postorder: remove this stone only after DFS children are processed.
        // Do not remove the root stone of this component.
        if (!isRoot) {
            removalOrder.push_back(node);
        }
    }
};