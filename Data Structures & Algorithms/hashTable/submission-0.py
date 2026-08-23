class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


    def hashfunction(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hashfunction(key)
        node = self.table[index]
        if node == None:
            node = Node(key, value)
            self.table[index] = node 
            self.size += 1
            if self.size >= self.capacity * 0.5:
                self.resize()
            return

        else:
            while node != None:
                if node.key == key:
                    node.value = value
                    return
                prev = node 
                node = node.next

            prev.next = Node(key, value)
            self.size +=1
            if self.size >= self.capacity * 0.5:
                self.resize()
            return
         



    def get(self, key: int) -> int:
        index = self.hashfunction(key)
        node = self.table[index]
        if node == None:
            return -1

        elif node.key == key:
            return node.value

        else:
            while node != None:
                if node.key == key:
                    return node.value
                else:
                    node = node.next

        return -1

       


    def remove(self, key: int) -> bool:
        index = self.hashfunction(key)
        node = self.table[index]
        if node == None:
            return False

        elif node.key == key:
            # if there is no chain set node to null
            if node.next == None:
                self.table[index] = None
                self.size -= 1
                return True
            else:
            # if there was a chain set the next element in the chain to the index
                self.table[index] = node.next
                self.size -= 1
                return True
            

        else:
            prev = None
            while node != None:
                
                if node.key == key:
                    if node.next == None:
                        prev.next = None
                        self.size -= 1
                        return True
                    else:
                        prev.next = node.next
                        self.size -= 1
                        return True

                prev = node 
                node = node.next 

                    
           

        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        oldcapacity = self.capacity
        newcapacity = 2 * self.capacity
        self.capacity = newcapacity
        newtable = [None] * newcapacity
        # Loop through old table get key and hash then place in new table
        for i in range(0, oldcapacity):
            node = self.table[i]
             
            # if the node exists hash its key to find index in new table
            while node != None:
                next_node = node.next 
                node.next = None 
                index = self.hashfunction(node.key)
                # place it in the new table at that index if it none else use node.next
                if newtable[index] == None:
                    newtable[index] = node
                # loop through (chaining) till you see a next pointer that is free and place it there
                else:
                    node2 = newtable[index]
                    while node2 != None:
                        if node2.next == None:
                            node2.next = node
                        
                        node2 = node2.next
                node = next_node





            

        self.table = newtable
        self.capacity = newcapacity
        return


