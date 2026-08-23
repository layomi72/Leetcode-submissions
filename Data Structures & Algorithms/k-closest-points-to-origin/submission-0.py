class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # hashmap mapping coordinates to their distances
        answer = []
        coordtodistance = {}
        for i in range(0,len(points)):
            coordtodistance[i] = ((points[i][0])**2 + (points[i][1])**2) * ((points[i][0])**2 + (points[i][1])**2)

        shortestdistances = []

        for val in coordtodistance.values():
            shortestdistances.append(val)

        heapq.heapify(shortestdistances)

        for i in range(0,k):
            point = heapq.heappop(shortestdistances)
            for key in coordtodistance:
                if coordtodistance[key] == point:
                    answer.append(points[key])

                    # 2. Add del to "claim" the point
                    del coordtodistance[key] 
                    
                    # 3. Add break to stop looking for this pop
                    break

        return answer