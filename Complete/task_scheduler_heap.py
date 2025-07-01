class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_h = [-x for x in count.values()]
        heapq.heapify(max_h)

        time = 0 
        q = deque()
        while max_h or q:
            time += 1

            # check max_h
            if not max_h:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_h)
                if cnt:
                    q.append([cnt, time + n])

            # check queue
            if q and q[0][1] == time:
                heapq.heappush(max_h, q.popleft()[0])

        return time