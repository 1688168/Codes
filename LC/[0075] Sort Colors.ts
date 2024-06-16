/**
 Do not return anything, modify nums in-place instead.
 */
 function sortColors(nums: number[]): void {
    let [i, l, r] = [0, 0, nums.length - 1];

    while (i <= r) {
        if (nums[i] === 0) {
            swap(i, l); 
            l += 1;
            i += 1;
        } else if (nums[i] === 2) {
            swap(i, r);
            r -= 1;
        } else {
            i += 1;
        }
    }

    function swap(m, n) {
        [nums[m], nums[n]] = [nums[n], nums[m]]; //typescript swap
    }
};

// const counts = [0,0,0];
// for (let i = 0; i < nums.length; i++) {
//     counts[nums[i]] += 1
// }
// let k = 0;
// for (let i = 0; i < counts.length; i++) {
//     for (let j = 0; j < counts[i]; j++) {
//         nums[k++] = i;
//     }
// }