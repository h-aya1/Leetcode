class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.vals.append(val)
        self.idx[val] = len(self.vals)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        
        self.vals.remove(val)
        del self.idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()