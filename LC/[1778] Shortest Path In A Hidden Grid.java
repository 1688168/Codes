import java.util.*;

class Solution {
    private static final char[] DIR = {'U', 'D', 'L', 'R'};
    private static final char[] BACK = {'D', 'U', 'R', 'L'};
    private static final int[][] DELTA = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    private static class Frame {
        int row, col;
        int nextDir;
        int enteredBy;

        Frame(int row, int col, int enteredBy) {
            this.row = row;
            this.col = col;
            this.enteredBy = enteredBy;
        }
    }

    // Encode two signed coordinates into one unique long.
    private long key(int row, int col) {
        return ((long) row << 32) | (col & 0xffffffffL);
    }

    public int findShortestPath(GridMaster master) {
        Set<Long> reachable = new HashSet<>();
        reachable.add(key(0, 0));

        Long target = master.isTarget() ? key(0, 0) : null;

        Deque<Frame> stack = new ArrayDeque<>();
        stack.push(new Frame(0, 0, -1));

        // 1. Explore and map the grid with DFS.
        while (!stack.isEmpty()) {
            Frame current = stack.peek();

            if (current.nextDir == 4) {
                stack.pop();
                if (current.enteredBy != -1) {
                    master.move(BACK[current.enteredBy]);
                }
                continue;
            }

            int d = current.nextDir++;
            int nr = current.row + DELTA[d][0];
            int nc = current.col + DELTA[d][1];
            long nextKey = key(nr, nc);

            if (reachable.contains(nextKey) || !master.canMove(DIR[d])) {
                continue;
            }

            master.move(DIR[d]);
            reachable.add(nextKey);

            if (master.isTarget()) {
                target = nextKey;
            }

            stack.push(new Frame(nr, nc, d));
        }

        if (target == null) {
            return -1;
        }

        // 2. BFS on the discovered grid.
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 0}); // row, col, distance
        reachable.remove(key(0, 0));

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int row = current[0];
            int col = current[1];
            int distance = current[2];

            if (key(row, col) == target.longValue()) {
                return distance;
            }

            for (int[] delta : DELTA) {
                int nr = row + delta[0];
                int nc = col + delta[1];

                // Removing on enqueue also marks the cell as visited.
                if (reachable.remove(key(nr, nc))) {
                    queue.offer(new int[]{nr, nc, distance + 1});
                }
            }
        }

        return -1;
    }
}