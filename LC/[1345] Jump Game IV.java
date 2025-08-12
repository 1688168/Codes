import java.util.*;

class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n == 1) return 0;

        // value -> all indices having that value
        Map<Integer, List<Integer>> val2idx = new HashMap<>();
        for (int i = 0; i < n; i++) {
            val2idx.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }

        boolean[] visited = new boolean[n];
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(0);
        visited[0] = true;

        int level = 0;
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int k = 0; k < sz; k++) {
                int curr = q.poll();

                // case I: curr + 1
                if (curr + 1 < n && !visited[curr + 1]) {
                    if (curr + 1 == n - 1) return level + 1;
                    visited[curr + 1] = true;
                    q.offer(curr + 1);
                }

                // case II: curr - 1
                if (curr - 1 >= 0 && !visited[curr - 1]) {
                    visited[curr - 1] = true;
                    q.offer(curr - 1);
                }

                // case III: all indices with the same value
                int val = arr[curr];
                List<Integer> same = val2idx.get(val);
                if (same != null) {
                    for (int next : same) {
                        if (!visited[next]) {
                            if (next == n - 1) return level + 1;
                            visited[next] = true;
                            q.offer(next);
                        }
                    }
                    // prune so we don't process this value again
                    val2idx.remove(val);
                }
            }
            level++;
            if (visited[n - 1]) return level;
        }

        return level;
    }
}
 