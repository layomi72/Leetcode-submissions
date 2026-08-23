class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequency = {}
        sorted_pairs = []
        answer = []

        for i in range(len(nums)):
            if nums[i] not in most_frequency:
                most_frequency[nums[i]] = 1
            else:
                 most_frequency[nums[i]] += 1

        # Create a list of sorted pairs based on the size of the value 
        sorted_pairs = sorted(most_frequency.items() , key=lambda p: p[1], reverse=True)

        for i in range(k):
            item = sorted_pairs[i]
            answer.append(item[0])
        
        return answer