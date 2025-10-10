class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key not in self.map:
            return value
        record = self.map[key]
        l, r = 0, len(record)-1
        
        while l <= r:
            mid = (r+l)//2
            if record[mid][0] <= timestamp:
                value = record[mid][1]
                l = mid+1
            elif record[mid][0] > timestamp:
                r = mid-1
        return value
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)