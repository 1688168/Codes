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
        }
    }

    private String encode(int x, int y) {
        return x + "#" + y;
    }

    public int findShortestPath(GridMaster master) {
        char[] directions = {'U', 'D', 'L', 'R'};
        char[] reverse = {'D', 'U', 'R', 'L'};
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        if (master.isTarget()) {
            return 0;
        }

        String start = encode(0, 0);
        Set<String> reachable = new HashSet<>();
        reachable.add(start);

        String target = null;

        // Iterative DFS to map the grid.
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
            String next = encode(nx, ny);

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

        // Keep coordinates in the queue to avoid parsing strings.
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0});
        reachable.remove(start);

        int distance = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int j = 0; j < size; j++) {
                int[] current = queue.poll();
                int x = current[0];
                int y = current[1];

                if (encode(x, y).equals(target)) {
                    return distance;
                }

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    String next = encode(nx, ny);

                    if (reachable.remove(next)) {
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }

            distance++;
        }

        return -1;
    }
}