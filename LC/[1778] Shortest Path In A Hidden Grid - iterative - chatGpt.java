import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    private static final char[] DIRECTIONS = {'U', 'D', 'L', 'R'};
    private static final char[] REVERSE_DIRECTIONS = {'D', 'U', 'R', 'L'};
    private static final int[][] COORDINATE_CHANGES = {
        {0, -1}, {0, 1}, {-1, 0}, {1, 0}
    };

    // Stores the state of a suspended DFS call.
    private static class Frame {
        private final int x;
        private final int y;
        private final int returnDirectionIndex;
        private int directionIndex;

        private Frame(int x, int y, int returnDirectionIndex) {
            this.x = x;
            this.y = y;
            this.returnDirectionIndex = returnDirectionIndex;
        }
    }

    private static String encode(int x, int y) {
        return x + "#" + y;
    }

    private static int[] decode(String code) {
        String[] parts = code.split("#");
        return new int[] {
            Integer.parseInt(parts[0]),
            Integer.parseInt(parts[1])
        };
    }

    public int findShortestPath(GridMaster master) {
        if (master.isTarget()) {
            return 0;
        }

        Set<String> reachable = new HashSet<>();
        Deque<Frame> stack = new ArrayDeque<>();
        String start = encode(0, 0);
        String target = "";

        reachable.add(start);
        stack.push(new Frame(0, 0, -1));

        // Map all reachable cells using iterative DFS.
        while (!stack.isEmpty()) {
            Frame frame = stack.peek();

            if (frame.directionIndex == DIRECTIONS.length) {
                // Restore the master's position to the parent cell.
                if (frame.returnDirectionIndex != -1) {
                    master.move(
                        REVERSE_DIRECTIONS[frame.returnDirectionIndex]
                    );
                }
                stack.pop();
                continue;
            }

            int directionIndex = frame.directionIndex++;
            int nx = frame.x + COORDINATE_CHANGES[directionIndex][0];
            int ny = frame.y + COORDINATE_CHANGES[directionIndex][1];
            String neighborCode = encode(nx, ny);

            if (reachable.contains(neighborCode)) {
                continue;
            }
            if (!master.canMove(DIRECTIONS[directionIndex])) {
                continue;
            }

            reachable.add(neighborCode);
            master.move(DIRECTIONS[directionIndex]);

            if (master.isTarget()) {
                target = neighborCode;
            }

            stack.push(new Frame(nx, ny, directionIndex));
        }

        if (target.isEmpty()) {
            return -1;
        }

        // Find the shortest distance using BFS on the mapped cells.
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(start);
        reachable.remove(start);
        int distance = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                String code = queue.poll();

                if (code.equals(target)) {
                    return distance;
                }

                int[] coordinates = decode(code);

                for (int directionIndex = 0;
                     directionIndex < DIRECTIONS.length;
                     directionIndex++) {
                    int nx = coordinates[0]
                        + COORDINATE_CHANGES[directionIndex][0];
                    int ny = coordinates[1]
                        + COORDINATE_CHANGES[directionIndex][1];
                    String neighborCode = encode(nx, ny);

                    // Removing on enqueue prevents duplicate visits.
                    if (reachable.remove(neighborCode)) {
                        queue.offer(neighborCode);
                    }
                }
            }

            distance++;
        }

        return -1;
    }
}