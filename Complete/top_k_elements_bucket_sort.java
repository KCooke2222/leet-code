class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();

        // Increment each element in the hash
        for (int i : nums) {
            count.put(i, count.getOrDefault(i, 0) + 1);
        }

        // Create array based on the freq of elements (freq is index)
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }


        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }
        
        int[] result = new int[k];

        int j = 0;
        for (int i = freq.length - 1; i > 0; i--) {
            for (int n : freq[i]) {
                result[j] = n;
                j++;
                if (j == k) {
                    return result;
                }
            }
        }

        return new int[] {0};
    }
}
