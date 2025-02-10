# fairly easy with sortedlist
class NumberContainers:

    def __init__(self):
        self.d = {}
        self.n = {}

    def change(self, index: int, number: int) -> None:
        if index in self.d:
            p = self.d[index]
            self.n[p].discard(index)

        self.d[index] = number
        if number in self.n:
            self.n[number].add(index)
        else:
            self.n[number] = SortedList([index])

    def find(self, number: int) -> int:
        if number in self.n and self.n[number]:
            return self.n[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)