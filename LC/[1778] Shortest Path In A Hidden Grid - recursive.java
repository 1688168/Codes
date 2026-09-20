import java.util.*;

class Solution {
    private static final char[] DIR = {'U', 'D', 'L', 'R'};
    private static final char[] BACK = {'D', 'U', 'R', 'L'};
    private static final int[][] DELTA = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    private final Set<Long> reachable = new HashSet<>();
    private Long target;

    private long key(int row, int col) {
        return ((long) row << 32) | (col & 0xffffffffL);
    }

    public int findShortestPath(GridMaster master) {
        reachable.clear();
        target = null;
        reachable.add(key(0, 0));

        dfs(master, 0, 0);

        if (target == null) {
            return -1;
        }

        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 0});
        reachable.remove(key(0, 0));

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0], col = cell[1], distance = cell[2];

            if (key(row, col) == target.longValue()) {
                return distance;
            }

            for (int[] delta : DELTA) {
                int nr = row + delta[0];
                int nc = col + delta[1];

                if (reachable.remove(key(nr, nc))) {
                    queue.offer(new int[]{nr, nc, distance + 1});
                }
            }
        }

        return -1;
    }

    private void dfs(GridMaster master, int row, int col) {
        if (master.isTarget()) {
            target = key(row, col);
        }

        for (int d = 0; d < 4; d++) {
            int nr = row + DELTA[d][0];
            int nc = col + DELTA[d][1];

            if (reachable.contains(key(nr, nc))
                    || !master.canMove(DIR[d])) {
                continue;
            }

            reachable.add(key(nr, nc));
            master.move(DIR[d]);
            dfs(master, nr, nc);
            master.move(BACK[d]); // Restore the robot's position.
        }
    }
}