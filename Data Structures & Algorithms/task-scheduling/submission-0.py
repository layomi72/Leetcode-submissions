class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskcount = {}
        max_count = 0

        for task in tasks:
            taskcount[task] = taskcount.get(task, 0) + 1

        max_frequency = max(taskcount.values())

        for k, v in taskcount.items():
            if v == max_frequency:
                max_count += 1

        
        return max(((max_frequency - 1) * (n + 1)) + max_count, len(tasks))
        