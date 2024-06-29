# hash, array, linked-list
class MyHashMap:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        t = self.eval_hash(key)
        for i, kv in enumerate(self.arr[t]):
            k, v = self.arr[t][i]
            if k == key:
                self.arr[t][i] = (key, value)
                break
        else:
            self.arr[t].append((key, value))


    def get(self, key: int) -> int:
        t = self.eval_hash(key)
        for i, kv in enumerate(self.arr[t]):
            k, v = self.arr[t][i]
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        for i, kv in enumerate(self.arr[t]):
            k, v = self.arr[t][i]
            if k == key:
                del self.arr[t][i]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)