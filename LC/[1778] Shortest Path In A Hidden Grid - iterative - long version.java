import java.util.*;

class Solution {
    private static class Cell {
        final int x, y;

        Cell(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (!(obj instanceof Cell)) {
                return false;
            }

            Cell other = (Cell) obj;
            return x == other.x && y == other.y;
        }

        @Override
        public int hashCode() {
            return (x * 73856093) ^ (y * 19349663);
        }
    }

    private static class Direction {
        final char move;
        final int dx, dy;
        final char reverse;

        Direction(char move, int dx, int dy, char reverse) {
            this.move = move;
            this.dx = dx;
            this.dy = dy;
            this.reverse = reverse;
        }
    }

    private static class Frame {
        final Cell position;
        int nextDirection;
        final char returnDirection;

        Frame(Cell position, char returnDirection) {
            this.position = position;
            this.returnDirection = returnDirection;
        }
    }

    public int findShortestPath(GridMaster master) {
        Direction[] directions = {
            new Direction('U',  0, -1, 'D'),
            new Direction('D',  0,  1, 'U'),
            new Direction('L', -1,  0, 'R'),
            new Direction('R',  1,  0, 'L')
        };

        if (master.isTarget()) {
            return 0;
        }

        Cell start = new Cell(0, 0);
        Set<Cell> reachable = new HashSet<>();
        reachable.add(start);

        Cell target = null;

        // Iterative DFS to map the grid.
        Deque<Frame> stack = new ArrayDeque<>();
        stack.push(new Frame(start, '\0'));

        while (!stack.isEmpty()) {
            Frame frame = stack.peek();

            if (frame.nextDirection == directions.length) {
                stack.pop();

                if (frame.returnDirection != '\0') {
                    master.move(frame.returnDirection);
                }
                continue;
            }

            Direction dir = directions[frame.nextDirection++];
            Cell next = new Cell(
                frame.position.x + dir.dx,
                frame.position.y + dir.dy
            );

            if (reachable.contains(next)) {
                continue;
            }
            if (!master.canMove(dir.move)) {
                continue;
            }

            master.move(dir.move);
            reachable.add(next);
            stack.push(new Frame(next, dir.reverse));

            if (master.isTarget()) {
                target = next;
            }
        }

        if (target == null) {
            return -1;
        }

        // BFS to find the shortest distance.
        Deque<Cell> queue = new ArrayDeque<>();
        queue.offerLast(start);
        reachable.remove(start);

        int distance = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                Cell current = queue.pollFirst();

                if (current.equals(target)) {
                    return distance;
                }

                for (Direction dir : directions) {
                    Cell next = new Cell(
                        current.x + dir.dx,
                        current.y + dir.dy
                    );

                    // Remove when enqueuing to mark it visited.
                    if (reachable.remove(next)) {
                        queue.offerLast(next);
                    }
                }
            }

            distance++;
        }

        return -1;
    }
}