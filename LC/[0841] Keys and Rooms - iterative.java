class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Deque<Integer> stack = new ArrayDeque<>();
        boolean[] visited = new boolean[rooms.size()];

        stack.push(0);
        visited[0] = true;
        int visitedCount = 1;

        while (!stack.isEmpty()) {
            int room = stack.pop();

            for (int key : rooms.get(room)) {
                if (!visited[key]) {
                    visited[key] = true;
                    visitedCount++;
                    stack.push(key);
                }
            }
        }

        return visitedCount == rooms.size();
    }
}