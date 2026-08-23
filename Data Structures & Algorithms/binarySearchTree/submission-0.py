class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = Node(key,val)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            
            while True:
                if current.key < newNode.key:
                    if current.right == None:
                        current.right = newNode
                        return
                    else:
                        current = current.right
            
                elif current.key > newNode.key:
                    if current.left == None:
                        current.left = newNode
                        return
                    else:
                            current = current.left
                elif current.key == newNode.key:
                    current.value = newNode.value
                    return 


    def get(self, key: int) -> int:
        current = self.root
        while True:
            if  current != None and current.key < key:
                current = current.right
            elif current != None and current.key > key:
                current = current.left
            elif current != None and current.key == key:
                return current.value
            else:
                return -1




    def getMin(self) -> int:
        if self.root == None:
            return -1
        else:
            current = self.root
            while True:
                if current.left == None:
                    return current.value
                else:
                    current = current.left
        
    def findMin(self, node: Node) -> Node:  # Returns a Node!
        if node == None:
            return None
        current = node
        while current.left != None:
            current = current.left
        return current  # Return the Node itself

    def getMax(self) -> int:
        if self.root == None:
            return -1
        else:
            current = self.root
            while True:
                if current.right == None:
                    return current.value
                else:
                    current = current.right


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)


    def removeHelper(self, current: Node, key: int) -> Node:

        if current == None:
            return None

        elif key < current.key:
            current.left = self.removeHelper(current.left,key)
            return current

        elif key > current.key:
            current.right = self.removeHelper(current.right, key)
            return current

        else:
            #if node has no children return none 
            if current.left == None and current.right == None:
                return None
            #if node has only a right child return right child
            elif current.left == None and current.right != None:
                return current.right
            #if node has only a left child return the left child
            elif current.left != None and current.right == None:
                return current.left
            else:
            #if node has two children find the inorder successor
                inOrderSuccessor = self.findMin(current.right)
                current.key = inOrderSuccessor.key
                current.value = inOrderSuccessor.value
                current.right = self.removeHelper(current.right,inOrderSuccessor.key)
                return current




        


    def getInorderKeys(self) -> List[int]:
        answer = []
        self.traversal(self.root, answer)
        return answer

    def traversal(self, root: Node,answer: List[int]) -> None:
       if root == None:
        return 

       self.traversal(root.left,answer)
       answer.append(root.key)
       self.traversal(root.right,answer)
        

