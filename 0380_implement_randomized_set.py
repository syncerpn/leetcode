# use dict, list, and counter
class RandomizedSet:

    def __init__(self):
        self.elements = {}
        self.counter = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements[val] = self.n
        self.counter += [val]
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.elements:
            i = self.elements[val]
            self.n -= 1

            last_element = self.counter[self.n]
            self.counter[i] = last_element
            self.elements[last_element] = i
            self.counter.pop()
            del self.elements[val]
            return True
        
        return False
    
    import random
    def getRandom(self) -> int:
        r = random.randint(0, self.n-1)
        return self.counter[r]