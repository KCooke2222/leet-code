class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}

        for t in tasks:
            task_count[t] = task_count.get(t, 0) + 1

        max_freq = max(task_count.values())
        num_max = sum(1 for v in task_count.values() if v == max_freq)

        # Calculate least time
        slots = (max_freq - 1) * (n + 1) + num_max # frames * frame size + other maxes
        return max(slots, len(tasks))