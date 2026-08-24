class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timemap:
            self.timemap[key] = [[value,timestamp]]
        else:
            self.timemap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        L = 0
        ans = ""

        #index 1 is the timestamp
        if key in self.timemap:
            array = self.timemap[key]
        else:
            return ""

        R = len(self.timemap[key]) - 1

        while L <= R:
            mid = ( L + R ) // 2
            if array[mid][1] <= timestamp:
                ans = array[mid][0]
                L = mid + 1

            else:
                R = mid - 1

    

        return ans
