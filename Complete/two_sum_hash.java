class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Hash the array
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        // Check for target - index (difference) in hash
        for (int i = 0; i < nums.length; i++) {
            int j = target - nums[i];
            if (map.containsKey(j) && i != map.get(j)) {
                return new int[] {i, map.get(j)};
            }
        }

        return new int[] {0};
    }
}
