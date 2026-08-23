class UnionFind:
    
    def __init__(self, n: int):
        self.root = []
        self.size = [0] * n
        self.no_of_roots = n

        for i in range(n):
            self.root.append(i)

    def find(self, x: int) -> int:
        # if the root of x equals it self then we have found the root
        # if x does not equal its root we set the parent of x to find(self.root[x]) (path compression)
        if  x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        else:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX

            elif self.size[rootY] > self.size[rootX]:
                self.root[rootX] = rootY

            else:
                self.root[rootY] = rootX
                self.size[rootX] += 1

            self.no_of_roots -= 1
            return True
        

    def getNumComponents(self) -> int:
        return self.no_of_roots