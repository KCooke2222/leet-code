class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.time_map[key]) - 1

        res = "" # no result
        while l <= r:
            mid = (l + r) // 2
            if self.time_map[key][mid][0] == timestamp:
                return self.time_map[key][mid][1] # target found
            elif self.time_map[key][mid][0] < timestamp:
                res = self.time_map[key][mid][1] # last valid
                l = mid + 1
            else:
                r = mid - 1

        return res