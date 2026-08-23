class Node:
    def __init__(self,val:int, key:int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
       
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.length = 0

        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.cache:
            returned = self.cache[key]

            self.remove(returned)
            self.insert(returned)
        
            return returned.val 
        
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
            if key in self.cache:
                node = self.cache[key]
                node.val = value
                self.remove(node)
                self.insert(node)

            else:
                node = Node(value, key)
                self.cache[key] = node
                # attach at the back
                self.insert(node)
                if len(self.cache) > self.capacity:
                    # remove self.head.next from the list AND from the dict                 
                    lru = self.head.next
                    self.remove(lru)
                    self.cache.pop(lru.key)

            

    def remove(self, x: Node) -> None:
        previous = x.prev
        nextt = x.next
        nextt.prev = previous
        previous.next = nextt

    def insert(self, x: Node) -> None:
        y = self.tail.prev
        y.next = x
        x.prev = y
        x.next = self.tail
        self.tail.prev = x


