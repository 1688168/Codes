class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int[] roots = new int[n]; //declare int array

        // Each city starts as its own root.
        for (int i = 0; i < n; i++) { //int array initialization
            roots[i] = i;
        }

        // Only traverse half of the matrix because it is symmetric.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    union(roots, i, j);
                }
            }
        }

        // Count unique root parents.
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (find(roots, i) == i) {
                count++;
            }
        }

        return count;
    }

    private void union(int[] roots, int a, int b) {
        int rootA = find(roots, a);
        int rootB = find(roots, b);

        if (rootA != rootB) {
            roots[rootA] = rootB;
        }
    }

    private int find(int[] roots, int x) {
        if (roots[x] != x) {
            roots[x] = find(roots, roots[x]); // path compression
        }

        return roots[x];
    }
}