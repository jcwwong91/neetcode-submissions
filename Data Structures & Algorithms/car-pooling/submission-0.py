class Solution:
    def carPooling(self, raw_trips: List[List[int]], capacity: int) -> bool:
        trips = list()
        for (passengers, start, stop) in raw_trips:
            heapq.heappush(trips, (start, passengers))
            heapq.heappush(trips, (stop, -passengers))
        
        passengers = 0
        while trips:
            location, changes = heapq.heappop(trips)
            passengers += changes
            if passengers > capacity:
                return False

        return True
            
            