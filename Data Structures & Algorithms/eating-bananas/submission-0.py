class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
      

        while L <= R:
            mid = (L + R) // 2
            hour = 0

            for pile in piles:
                hour += math.ceil(pile/mid)

            if  hour <= h:
                R = mid - 1
            
            else: 
                L = mid + 1


        return  L