class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return  True
        else:
            return False

    def append(self, value: int) -> None:
        valuetoinsert = Node(value)
        if self.isEmpty() == False:
            previouslastnode = self.tail.prev
            self.tail.prev = valuetoinsert
            self.tail.prev.prev = previouslastnode
            previouslastnode.next = valuetoinsert
            self.tail.prev.next = self.tail
        else:
            self.head.next = valuetoinsert
            valuetoinsert.next = self.tail
            valuetoinsert.prev = self.head
            self.tail.prev = valuetoinsert
        

    def appendleft(self, value: int) -> None:
        previousfirstnode = self.head.next
        valuetoinsert = Node(value)
        if self.isEmpty() == True:
            self.head.next = valuetoinsert
            self.tail.prev = valuetoinsert
            valuetoinsert.next = self.tail
            valuetoinsert.prev = self.head
        else:
            self.head.next = valuetoinsert
            valuetoinsert.next = previousfirstnode
            valuetoinsert.prev = self.head
            previousfirstnode.prev = valuetoinsert


        

    def pop(self) -> int:
        if self.isEmpty() == True:
            return - 1
        else:
            previouslastnode = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

            return previouslastnode.value

    def popleft(self) -> int:
        previousfirstnode = self.head.next
        if self.isEmpty() == True:
            return -1
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return previousfirstnode.value

        
