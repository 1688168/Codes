import java.util.*;

class Solution {
    private static class Frame {
        int x, y;
        int nextDirection;
        char returnDirection;

        Frame(int x, int y, char returnDirection) {
            this.x = x;
            this.y = y;
            this.returnDirection = returnDirection;
            this.nextDirection = 0;
        }
    }

    // Pack two signed int coordinates into a unique long.
    private long encode(int x, int y) {
        return ((long) x << 32) | (y & 0xffffffffL);
    }

    public int findShortestPath(GridMaster master) {
        char[] directions = {'U', 'D', 'L', 'R'};
        char[] reverse = {'D', 'U', 'R', 'L'};
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        if (master.isTarget()) {
            return 0;
        }

        long start = encode(0, 0);
        Set<Long> reachable = new HashSet<>();
        reachable.add(start);

        Long target = null;

        // Iterative DFS to map the reachable cells.
        Deque<Frame> stack = new ArrayDeque<>();
        stack.push(new Frame(0, 0, '\0'));

        while (!stack.isEmpty()) {
            Frame frame = stack.peek();

            if (frame.nextDirection == 4) {
                stack.pop();
                if (frame.returnDirection != '\0') {
                    master.move(frame.returnDirection);
                }
                continue;
            }

            int i = frame.nextDirection++;
            int nx = frame.x + dx[i];
            int ny = frame.y + dy[i];
            long next = encode(nx, ny);

            if (reachable.contains(next)) {
                continue;
            }
            if (!master.canMove(directions[i])) {
                continue;
            }

            master.move(directions[i]);
            reachable.add(next);
            stack.push(new Frame(nx, ny, reverse[i]));

            if (master.isTarget()) {
                target = next;
            }
        }

        if (target == null) {
            return -1;
        }

        // BFS to find the shortest distance.
        // Removing a cell from reachable marks it visited.
        Deque<Long> queue = new ArrayDeque<>();
        queue.offer(start);
        reachable.remove(start);

        int distance = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int j = 0; j < size; j++) {
                long current = queue.poll();

                if (current == target.longValue()) {
                    return distance;
                }

                int x = (int) (current >> 32);
                int y = (int) current;

                for (int i = 0; i < 4; i++) {
                    long next = encode(x + dx[i], y + dy[i]);

                    if (reachable.remove(next)) {
                        queue.offer(next);
                    }
                }
            }

            distance++;
        }

        return -1;
    }
}