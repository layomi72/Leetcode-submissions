import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue

            elif  -x < -y:
                heapq.heappush(heap,-(x - y))

            else:
                if -x > -y:
                    heapq.heappush(heap,-(y - x))


        if not heap:
            return 0

        else:
            return -heap[-1]


        