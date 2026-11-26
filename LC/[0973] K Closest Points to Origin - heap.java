class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
        //     (a, b) -> Long.compare(distanceSquared(b), distanceSquared(a))
        // );

        // PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
        //     Comparator.comparingLong(
        //         (int[] point) -> distanceSquared(point)
        //     ).reversed()
        // );

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            Comparator.<int[]>comparingLong(
                point -> distanceSquared(point)
            ).reversed()
        );

        for (int[] point : points) {
            maxHeap.offer(point);
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }

        return maxHeap.toArray(new int[maxHeap.size()][]);
    }

    private long distanceSquared(int[] point) {
        return (long) point[0] * point[0] + (long) point[1] * point[1];
    }
}