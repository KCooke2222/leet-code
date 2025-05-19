class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        // Increment each element in the hash
        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        // Sort the hash by value and return corresponding keys (using arraylist)
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(map.entrySet());

        entries.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        List<Map.Entry<Integer, Integer>> topk = entries.subList(0, k);

        int[] topKeys = new int[k];

        int i = 0;
        for (Map.Entry<Integer, Integer> entry : topk) {
            topKeys[i] = entry.getKey();
            i++;
        }

        return topKeys;
    }
}
