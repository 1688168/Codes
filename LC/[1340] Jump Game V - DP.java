import java.util.*;

class Solution {
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        // Sort indices by height ascending (compute from lower to higher)
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> arr[a] != arr[b] ? Integer.compare(arr[a], arr[b]) : Integer.compare(a, b));

        for (int k = 0; k < n; k++) {
            int i = idx[k];

            // Look right
            for (int j = i + 1; j <= Math.min(n - 1, i + d); j++) {
                if (arr[j] >= arr[i]) break;                 // blocked
                dp[i] = Math.max(dp[i], 1 + dp[j]);          // pull from lower
            }
            // Look left
            for (int j = i - 1; j >= Math.max(0, i - d); j--) {
                if (arr[j] >= arr[i]) break;                 // blocked
                dp[i] = Math.max(dp[i], 1 + dp[j]);          // pull from lower
            }
        }

        int ans = 0;
        for (int v : dp) ans = Math.max(ans, v);
        return ans;
    }
}