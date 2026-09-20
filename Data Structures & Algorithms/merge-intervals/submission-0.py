class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda p:p[0])
        if not intervals:
            return []
        
        answer = [sorted_intervals[0]]
        sorted_intervals.remove(sorted_intervals[0])

        for start, end in sorted_intervals:
            current_end = answer[-1][1]

            if start <= current_end:
                answer[-1][1] = max(current_end, end)

            else:
                answer.append([start,end])

        return answer