"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        sorted_intervals = sorted(intervals, key = lambda x:x.start)


        current = [sorted_intervals[0]]

        sorted_intervals.remove(sorted_intervals[0])


        for x in sorted_intervals:

            if x.start < current[-1].end:
                return False

            else:
                current.append(x)

        return True
