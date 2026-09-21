"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        rooms, count, s, e = 0,0,0,0
     
        for x in intervals:
            start.append(x.start)
            end.append(x.end)

        start.sort()
        end.sort()

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                rooms = max(rooms, count)
                s +=1
            
            else:
                count -= 1
                rooms = max(rooms, count)
                e += 1

        
        return rooms

            
               
        

    