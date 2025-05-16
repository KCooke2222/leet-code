class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Hold code and index in array
        HashMap<String, List<String>> map = new HashMap<>();

        // Convert strings to array code 
        for (int i = 0; i < strs.length; i++) {
            String word = strs[i];
            int[] code = new int[26];

            for (char c : word.toCharArray()) {
                code[c - 'a'] += 1;
            }
            String key = Arrays.toString(code);

            // Make hash with these codes matches to index in og array
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(strs[i]);
        }

        // Create list by code
        List<List<String>> result = new ArrayList<>();
        for (List<String> val : map.values()) {
            result.add(val);
        }

        return result;

    }
}
