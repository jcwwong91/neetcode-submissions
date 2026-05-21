class TimeMap:

    def __init__(self):
        self.values = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = list()
        self.values[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        values = self.values[key]
        print(key, timestamp, values)

        for i in range(len(values)-1, -1, -1):
            ts = values[i][0]
            if ts <= timestamp:
                return values[i][1]
        
        return ""

        """
        l = 0
        r = len(values)

        while True:
            m = (r + l) / 2
            print(l, m, r)
        """
            

        
        return "a"
        
