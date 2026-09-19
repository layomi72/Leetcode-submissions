class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}
        answer = []

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        
        sorted_frequency = sorted(frequency.items(), key = lambda p:(p[1], -p[0]))

        for key, value in sorted_frequency:
            for i in range(value):
                answer.append(key)

        return answer