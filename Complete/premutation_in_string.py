class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = defaultdict(int)
        s2_counts = defaultdict(int)
        l = 0

        for c in s1:
            s1_counts[c] += 1

        for r in range(len(s2)):
            # adjust left side
            if r-l >= len(s1):
                s2_counts[s2[l]] -= 1
                # adjust 0s (for comparison)
                if s2_counts[s2[l]] == 0:
                    del s2_counts[s2[l]]
                l += 1

            # add right side
            s2_counts[s2[r]] += 1

            # compare maps
            if (s1_counts == s2_counts):
                return True


        return False