class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n];   // diff[k] = delta score when rotation is k
        int maxScore = -1;
        int bestK = 0;

        for (int i = 0; i < n; i++) {
            int v = nums[i];

            if (v > i) {
                // events[(i+1)%n] += 1
                diff[(i + 1) % n] += 1;

                // events[(i+1 + n - v) % n] -= 1
                diff[(i + 1 + n - v) % n] -= 1;

                // events[0] += 0  (no-op)
            } else {
                // events[0] += 1
                diff[0] += 1;

                // events[(i - v + 1) % n] -= 1
                diff[(i - v + 1) % n] -= 1;

                // events[(i+1) % n] += 1
                diff[(i + 1) % n] += 1;
            }
        }

        int score = 0;
        for (int k = 0; k < n; k++) {
            score += diff[k];
            if (score > maxScore) {
                maxScore = score;
                bestK = k;
            }
        }
        return bestK;
    }
}
