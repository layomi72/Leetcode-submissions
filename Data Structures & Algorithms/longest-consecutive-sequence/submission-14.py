class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # write an array that stores the longest consecutive sequence for each index in nums
        sorted_list = sorted(set(nums))

        max_count = 1
        count = 1
        for i in range(len(sorted_list)):

            if i + 1 == len(sorted_list):
                max_count = max(max_count,count)
                continue
            if sorted_list[i + 1] - sorted_list[i] == 1:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 1

        return max_count