/* Top-Down Approach */

func maxCoins(nums []int) int {  
    nums = append(nums, 1)
    temp := []int{1}
    temp = append(temp, nums...)
    nums = temp
    n := len(nums)
    
    cache := make([][]int, n)
    for r := 0; r < n; r++ {
        cache[r] = make([]int, n)
    }    
    
    return dp(nums, 1, len(nums)-2, cache)
}

func dp(nums []int, left, right int, cache [][]int) int {
    if left > right {
        return 0
    }
    
    if cache[left][right] > 0 {
        return cache[left][right]
    }
    
    res := 0
    for i := left; i <= right; i++ {
        cGain := nums[left-1] * nums[i] * nums[right+1]
        lGain := dp(nums, left, i-1, cache)
        rGain := dp(nums, i+1, right, cache)
        res = max(res, cGain + lGain + rGain)
    }
    
    cache[left][right] = res
    return res
}