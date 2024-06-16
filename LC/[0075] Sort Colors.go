func sortColors(nums []int)  {
    N := len(nums)
    ii, jj, kk:= 0, 0, N-1

    for zz := 0; zz < N; zz++ {
        if jj>kk {break}
        if nums[jj] < 1 {
            nums[ii], nums[jj] = nums[jj], nums[ii]
            ii++
            jj++
        }else if nums[jj] == 1{
            jj++
        }else{
            nums[jj], nums[kk] = nums[kk], nums[jj]
            kk--
        }

    }
}

