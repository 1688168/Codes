import java.util.*;

class Solution {
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        int[] memo = new int[n]; // 0 means uncomputed
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dfs(i, arr, d, memo));
        }
        return ans;
    }

    private int dfs(int i, int[] arr, int d, int[] memo) {
        if (memo[i] != 0) return memo[i];
        int n = arr.length;
        int best = 1;

        // Explore to the right
        for (int j = i + 1; j <= Math.min(n - 1, i + d); j++) {
            if (arr[j] >= arr[i]) break;         // blocked by equal/higher
            best = Math.max(best, 1 + dfs(j, arr, d, memo));
        }

        // Explore to the left
        for (int j = i - 1; j >= Math.max(0, i - d); j--) {
            if (arr[j] >= arr[i]) break;         // blocked by equal/higher
            best = Math.max(best, 1 + dfs(j, arr, d, memo));
        }

        memo[i] = best;
        return best;
    }
}