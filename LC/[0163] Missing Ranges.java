import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        if (n == 0) {
            result.add(List.of(lower, upper));
            return result;
        }

        if (lower < nums[0]) {
            result.add(List.of(lower, nums[0] - 1));
        }

        int i = 0;
        while (i < n - 1) {
            while (i + 1 < n && nums[i] + 1 == nums[i + 1]) {
                i++;
            }

            if (i == n - 1) {
                break;
            }

            int left = nums[i] + 1;
            int right = nums[i + 1] - 1;
            result.add(List.of(left, right));
            i++;
        }

        if (nums[n - 1] < upper) {
            result.add(List.of(nums[n - 1] + 1, upper));
        }

        return result;
    }
}