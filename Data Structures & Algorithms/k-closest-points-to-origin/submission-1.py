class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance = {}
        heap = []
        answer = []
        for point in points:
            points_distance[(point[0],point[1])] = (point[0] * point[0]) + (point[1] * point[1])

        
        for value in points_distance.values():
            heapq.heappush(heap,value)

        smallest_distances = heapq.nsmallest(k, heap)

        for key, val in points_distance.items():
            if val in smallest_distances:
                answer.append(key)
        

        return answer
