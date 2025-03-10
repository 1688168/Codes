class Solution {
    public int tallestBillboard(int[] rods) {
        int N = rods.length;
        int offset = 5000;
        int[] dp = new int[offset * 2 + 5];// rods=[0, N], diff=[-5k, 5k]

        // initialize int array to a specific value
        dp = Arrays.stream(dp).map(x -> -1).toArray();

        // initialize DP
        dp[0 + offset] = 0;// start from maz height as zero when we have nothing

        // int [] dp_old = new int[offset*2+5];
        for (int ii = 0; ii < N; ++ii) {
            // clone the old dp
            // IntStream.range(0, N+1).map(idx -> dp_old[idx]=dp[idx]);
            int[] dp_old = dp.clone(); // Java how to copy array
            int ll = rods[ii];

            for (int jj = -offset; jj <= offset; ++jj) {// we don't need to contribute in end last use case
                if (jj - ll >= -offset && dp_old[jj - ll + offset] != -1) { // added left from old
                    dp[jj + offset] = Math.max(dp[jj + offset], dp_old[jj - ll + offset]+ll);
                }

                if (jj + ll <= offset && dp_old[jj + ll + offset] != -1) {
                    dp[jj + offset] = Math.max(dp[jj + offset], dp_old[jj + ll + offset]);
                }
            }
        }

        return dp[0 + offset];// max height for diff=0
    }
}