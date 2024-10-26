func maxCoins(nums []int) int {
    temp := []int{1}
    temp = append(temp, nums...)
    temp = append(temp, 1)
    nums = temp
    n := len(nums)
    
    dp := make([][]int, n)
    for r := 0; r < n; r++ {
        dp[r] = make([]int, n)
    }
    
    for left := n-2; left >= 1; left-- {
        for right := left; right <= n-2; right++ {
            for i := left; i <= right; i++ {
                cGain := nums[left-1] * nums[i] * nums[right+1]
                remaining := dp[left][i-1] + dp[i+1][right]
                dp[left][right] = max(dp[left][right], cGain + remaining)
            }
        }
    }
    
    return dp[1][n-2]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}