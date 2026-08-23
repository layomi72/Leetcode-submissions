class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        # whilst node is smaller than parent move it up
        index = len(self.heap) - 1
        while self.heap[index] < self.heap[index // 2] and index > 1:
            parent = self.heap[index // 2]
            child = self.heap[index]
            #swap the position of the parent and the child
            self.heap[index] = parent
            self.heap[index // 2] = child

            index = index // 2



    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        
        # Save smallest element to return
        smallestelement = self.heap[1]
        
        # Move last item to root and remove it
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        
        # Down-heapify
        start = 1
        while start * 2 < len(self.heap):
            left_child = start * 2
            right_child = start * 2 + 1
            
            # Find smaller child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smaller_child = right_child
            else:
                smaller_child = left_child
            
            # Swap parent with smaller child
            if self.heap[start] > self.heap[smaller_child]:
                self.heap[start], self.heap[smaller_child] = self.heap[smaller_child], self.heap[start]
                start = smaller_child
            break
        
        return smallestelement



        

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0]
        for i in range(0,len(nums)):
            self.push(nums[i])
        
        