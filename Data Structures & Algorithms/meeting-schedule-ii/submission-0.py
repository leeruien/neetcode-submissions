"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count_room = 0
        intervals.sort(key = lambda x: x.start)
        pq = []
        for i in intervals:
            start = i.start
            end = i.end
            if pq == []:
                if count_room == 0:
                    count_room += 1
                heapq.heappush(pq, end)
            else:
                if start >= pq[0]: # can fit 
                    heapq.heappop(pq)
                    
                elif (start < pq[0]) and (len(pq) == count_room):
                    count_room += 1

                heapq.heappush(pq, end)
        return count_room
            


        