class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sort = sorted(nums)
        l = 0
        r = len(nums) - 1
        ans = []
        seen = set()



        for i in range(len(sort)):

            if sort[i] in seen:
                continue
                
            else:
                
                seen.add(sort[i])

            l = i + 1

            r = len(nums) - 1
            target = 0 - sort[i]
            

            while l < r:

                total  = sort[l] + sort[r]

                if sort[l] + sort[r] == target:
                    if [sort[i],sort[l],sort[r]] not in ans:
                        ans.append([sort[i],sort[l],sort[r]])
                    l += 1
                    r -= 1

                elif total > target:
                    r -= 1
                    total  = sort[l] + sort[r]

                elif total < target:
                    l += 1
                    total  = sort[l] + sort[r]
                
   
        
        return ans


