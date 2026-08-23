class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []

        self.graph[src].append(dst)



    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph[src]:
            return False
        else:
            self.graph[src].remove(dst)
            return True



    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()

        visited.add(src)
        queue.append(src)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in self.graph[node]:
                    if neighbour == dst:
                        return True

                    else:
                        queue.append(neighbour)

        return False
                        

