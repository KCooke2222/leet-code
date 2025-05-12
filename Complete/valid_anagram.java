class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();

        // Sort using bubble sort
        bubbleSort(sc);
        bubbleSort(tc);

        // Compare strings for equality
        if (sc.equals(tc)) {
            return true;
        }
        return false;
    }

    private void bubbleSort(char[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    char temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}
