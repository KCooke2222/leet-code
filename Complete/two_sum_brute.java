class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Iterate all possibilities
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = nums.length - 1; j > i; j--) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }    
            }
        }

        return new int[] {0};
    }
}
