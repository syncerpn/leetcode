# we store {frequency: [keys]} and a double linked list to keep them sorted
class AllOne:

    def __init__(self):
        self.dll, self.key_counter = DoubleLinkedList(), {}
        self.f = {0: self.dll.get_sentinel_head()}

    def _remove_key_pf_node(self, pf, key):
        node = self.f[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.f.pop(pf)

    def inc(self, key: str) -> None:
        if key not in self.key_counter:
            self.key_counter[key] = 0
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key] - 1
        if cf not in self.f:
            self.f[cf] = self.dll.insert_after(self.f[pf])
        self.f[cf].add_key(key)
        if pf > 0:
            self._remove_key_pf_node(pf, key)

    def dec(self, key: str) -> None:
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key] + 1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.f:
                    self.f[cf] = self.dll.insert_before(self.f[pf])
                self.f[cf].add_key(key)
            self._remove_key_pf_node(pf, key)

    def getMaxKey(self) -> str:
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self) -> str:
        return self.dll.get_head().get_any_key() if self.dll.get_head().count() > 0 else ""

class Node:
    def __init__(self):
        self.key_set = set()
        self.p, self.n = None, None
    
    def add_key(self, key):
        self.key_set.add(key)
    
    def remove_key(self, key):
        self.key_set.discard(key)
    
    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def count(self):
        return len(self.key_set)
    
    def is_empty(self):
        return len(self.key_set) == 0

class DoubleLinkedList():
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.n, self.tail.p = self.tail, self.head
    
    def insert_after(self, x):
        node, t = Node(), x.n
        x.n, node.p = node, x
        node.n, t.p = t, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.p)
    
    def remove(self, x):
        prev_node = x.p
        prev_node.n, x.n.p = x.n, prev_node
    
    def get_head(self):
        return self.head.n
    
    def get_tail(self):
        return self.tail.p
    
    def get_sentinel_head(self):
        return self.head
    
    def get_sentinel_tail(self):
        return self.tail
    
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()