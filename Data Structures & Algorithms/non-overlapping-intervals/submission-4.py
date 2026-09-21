class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_intervals = sorted(intervals, key = lambda p:p[0])
        current = sorted_intervals[0]


        for start, end in sorted_intervals[1:]:
            if start < current[1]:
                count += 1
                current = [start, min(current[1], end)]
            else:
                current = [start, end]


        return count
            

            
