import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # choose two heaviest stones
        for i in range(0,len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        #if they equal each other remove both
       
        while len(stones) > 1:
            x = heapq.heappop(stones)
            x = -x
            y = heapq.heappop(stones)
            y = -y
            if x != y:
                if x < y:
                    y = (-y) - (-x)
                    y = -y
                    heapq.heappush(stones,y)
                else:
                    x = x - y
                    x = -x
                    heapq.heappush(stones,x)
        
        if stones == []:
            return 0
        else:
            return -heapq.heappop(stones)
        


        