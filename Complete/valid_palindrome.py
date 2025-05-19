class Solution:
    def isPalindrome(self, s: str):
        # remove case and non alphanumeric 
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True