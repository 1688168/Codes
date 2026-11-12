class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length;
        int i = 0;
        int maxDistance = 0;

        while (i < n) {
            // Skip occupied seats.
            while (i < n && seats[i] == 1) {
                i++;
            }

            if (i == n) {
                break;
            }

            int start = i;

            // Find the end of this empty range.
            while (i < n && seats[i] == 0) {
                i++;
            }

            int dist;

            if (start == 0 || i == n) {
                dist = i - start;
            } else {
                int leftOccupied = start - 1;
                int rightOccupied = i;
                dist = (rightOccupied - leftOccupied) / 2;
            }

            maxDistance = Math.max(maxDistance, dist);
        }

        return maxDistance;
    }
}