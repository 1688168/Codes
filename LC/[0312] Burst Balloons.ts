function maxCoins(nums: number[]): number {
    const n = nums.length;

    //ts: how to insert to array
    const extendedNums = [1, ...nums, 1]; // Add 1 before and after nums array, ts spreading. ts insert array

    // Initialize the DP table
    //ts: how to initialize an array with defined size
    //ts: how to generate an array
    //ts: generate a list of undefined with size (n+2)
    //ts: each undefined then is mapped to an array of size (n+2) and initialized with 0
    const dp: number[][] = Array.from({ length: n + 2 }, () => Array(n + 2).fill(0));

    // Fill the DP table
    for (let length = 1; length <= n; length++) {
        for (let left = 1; left <= n - length + 1; left++) {
            const right = left + length - 1;
            for (let i = left; i <= right; i++) {
                dp[left][right] = Math.max(
                    dp[left][right],
                    dp[left][i - 1] + extendedNums[left - 1] * extendedNums[i] * extendedNums[right + 1] + dp[i + 1][right]
                );
            }
        }
    }

    return dp[1][n];
}