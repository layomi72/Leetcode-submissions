class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        sortedcount = []

        for num in nums:
            if num in count:
                count[num] += 1 
            else:
                count[num] = 1

        sortedcount = sorted(count.items(), key = lambda p:p[1], reverse = True)

        return sortedcount[0][0]