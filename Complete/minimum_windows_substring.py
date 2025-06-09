class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_counts = defaultdict(int)
        t_counts = Counter(t)
        l = 0
        min_len = float("inf")
        min_window = ""

        for r in range(len(s)):
            s_counts[s[r]] += 1

            while l < len(s) and (s[l] not in t_counts or s_counts[s[l]] > t_counts[s[l]]):
                s_counts[s[l]] -= 1
                l += 1

            valid = True
            for c in t_counts:
                if s_counts[c] < t_counts[c]:
                    valid = False
                    break

            if valid and r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = s[l:r+1]

        return min_window
