import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        /*
         * Kahn's algorithm for topological sorting.
         *
         * An edge prerequisite -> course means that the
         * prerequisite must be completed before the course.
         */

        List<List<Integer>> graph = new ArrayList<>();

        for (int course = 0; course < numCourses; course++) {
            graph.add(new ArrayList<>());
        }

        int[] indegree = new int[numCourses];

        // Build the directed graph.
        for (int[] prerequisitePair : prerequisites) {
            int course = prerequisitePair[0];
            int prerequisite = prerequisitePair[1];

            graph.get(prerequisite).add(course);
            indegree[course]++;
        }

        // Add every course with no prerequisites.
        Queue<Integer> queue = new ArrayDeque<>();

        for (int course = 0; course < numCourses; course++) {
            if (indegree[course] == 0) {
                queue.offer(course);
            }
        }

        int[] order = new int[numCourses];
        int orderIndex = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[orderIndex++] = course;

            for (int nextCourse : graph.get(course)) {
                indegree[nextCourse]--;

                if (indegree[nextCourse] == 0) {
                    queue.offer(nextCourse);
                }
            }
        }

        // Not every course was processed, so a cycle exists.
        if (orderIndex != numCourses) {
            return new int[0];
        }

        return order;
    }
}