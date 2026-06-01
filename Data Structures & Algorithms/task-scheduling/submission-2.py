class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskmap = dict()
        for task in tasks:
            taskmap[task] = taskmap.get(task, 0) + 1

        maxf = 0
        maxCount = 0
        for k, v in taskmap.items():
            if v > maxf:
                maxf = v
                maxCount = 0
            if v == maxf:
                maxCount += 1

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
