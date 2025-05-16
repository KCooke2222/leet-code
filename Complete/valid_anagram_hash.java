class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();

        // Create 2 dicts to store each letter count
        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        for (char ch : sc) {
            smap.put(ch, smap.getOrDefault(ch, 0) + 1);
        }
        for (char ch : tc) {
            tmap.put(ch, tmap.getOrDefault(ch, 0) + 1);
        }

        // Compare dicts
        if (smap.equals(tmap)) {
            return true;
        }
        return false;
        
    }

}
