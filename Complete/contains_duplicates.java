class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0) {
            return false;
        }
        
        // Sort array
        Arrays.sort(nums);

        // Traverse checking prev value
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (prev == nums[i]) {
                return true;
            }
            prev = nums[i];
        }
        return false;
    }
}
