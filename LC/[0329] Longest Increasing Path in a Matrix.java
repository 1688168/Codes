class Solution {
    private int[][] matrix;
    private int[][] memo;
    private int rows;
    private int cols;

    private static final int[][] DIRECTIONS = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        this.matrix = matrix;
        this.rows = matrix.length;
        this.cols = matrix[0].length;
        this.memo = new int[rows][cols];

        int longestPath = 0;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                longestPath = Math.max(longestPath, dfs(row, col));
            }
        }

        return longestPath;
    }

    private int dfs(int row, int col) {
        if (memo[row][col] != 0) {
            return memo[row][col];
        }

        int longest = 1;

        for (int[] direction : DIRECTIONS) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];

            if (
                nextRow < 0 || nextRow >= rows ||
                nextCol < 0 || nextCol >= cols
            ) {
                continue;
            }

            if (matrix[nextRow][nextCol] <= matrix[row][col]) {
                continue;
            }

            longest = Math.max(
                longest,
                1 + dfs(nextRow, nextCol)
            );
        }

        memo[row][col] = longest;
        return longest;
    }
}