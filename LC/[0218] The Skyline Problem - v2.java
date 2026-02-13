import java.util.*;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        // Each building [L, R, H] becomes two events:
        // (L, -H) start   -> negative height so it sorts before end at same x
        // (R, +H) end
        List<int[]> events = new ArrayList<>(buildings.length * 2);
        for (int[] b : buildings) {
            int L = b[0], R = b[1], H = b[2];
            events.add(new int[]{L, -H});
            events.add(new int[]{R,  H});
        }

        // Sort by:
        // 1) x ascending
        // 2) height ascending (so starts (-H) come before ends (+H) at same x;
        //    also taller starts processed first because -15 < -10)
        events.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        // Max-heap for current heights (store positive heights, comparator reversed)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        // Frequency map for lazy deletion / accurate counts
        Map<Integer, Integer> freq = new HashMap<>();

        // Initialize with ground height 0
        maxHeap.offer(0);
        freq.put(0, 1);

        List<List<Integer>> result = new ArrayList<>();
        int prevMax = 0;

        int i = 0;
        while (i < events.size()) {
            int x = events.get(i)[0];

            // Process all events at the same x together
            while (i < events.size() && events.get(i)[0] == x) {
                int h = events.get(i)[1];

                if (h < 0) { // start
                    int height = -h;
                    maxHeap.offer(height);
                    freq.put(height, freq.getOrDefault(height, 0) + 1);
                } else { // end
                    int height = h;
                    freq.put(height, freq.get(height) - 1);
                }
                i++;
            }

            // Clean heap top: remove heights that are no longer active
            while (!maxHeap.isEmpty() && freq.getOrDefault(maxHeap.peek(), 0) == 0) {
                maxHeap.poll();
            }

            int currMax = maxHeap.peek();
            if (currMax != prevMax) {
                result.add(Arrays.asList(x, currMax));
                prevMax = currMax;
            }
        }

        return result;
    }
}