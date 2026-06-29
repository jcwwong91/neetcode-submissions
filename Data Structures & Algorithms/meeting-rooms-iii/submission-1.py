class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings_held = [0] * n
        avail = list()
        for i in range(n):
            heapq.heappush(avail, i)

        meetings.sort()
        print(meetings)
        done = list()
        i = 0
        current = 0
        while i < len(meetings):

            while (done and done[0][0] < meetings[i][0]) or not avail:
                end, room = heapq.heappop(done)
                current = end
                heapq.heappush(avail, room)
            
            start, end = meetings[i]
            current = max(current, start)
            i += 1
            print("avail", avail, start, end)
            room = heapq.heappop(avail)
            meetings_held[room] += 1
            print("meetings", meetings_held)
            duration = end-start
            heapq.heappush(done, (current + duration, room))
        

        ret = None
        count = 0
        for room in range(n):
            held = meetings_held[room]
            if held > count:
                count = held
                ret = room
        
        return ret

        