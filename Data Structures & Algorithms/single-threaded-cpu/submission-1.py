class Solution:
    def getOrder(self, raw_tasks: List[List[int]]) -> List[int]:
        
        tasks = list()
        for i in range(len(raw_tasks)):
            tasks.append((raw_tasks[i][0], raw_tasks[i][1], i))

        tasks.sort()
        heap = list()
        ret = list()

        heapq.heappush(heap, (tasks[0][1], tasks[0][2]))
        cur_time = tasks[0][0]
        i = 1
        while True:
            while i < len(tasks) and tasks[i][0] <= cur_time:
                start, proc, id = tasks[i]
                heapq.heappush(heap, (proc, id))
                i += 1

            if not heap:
                if i >= len(tasks):
                    break
                cur_time, proc, id = tasks[i]
                heapq.heappush(heap, (proc, id))
                i += 1
                continue
            
            proc, task_id = heapq.heappop(heap)
            cur_time += proc
            ret.append(task_id)

        return ret
        