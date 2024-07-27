# iterator in iterator
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.charset = characters
        self.i = 0
        self.n = combinationLength
        self.sub = None
        # make sub iterator for the next characters
        if self.n > 1:
            self.sub = CombinationIterator(self.charset[self.i+1:], self.n-1)

    def next(self) -> str:
        r = self.charset[self.i]
        if self.sub is None:
            self.i += 1
        else:
            r += self.sub.next()
            if not self.sub.hasNext():
                self.i += 1
                # remake sub iterator because the current one has expired
                self.sub = CombinationIterator(self.charset[self.i+1:], self.n-1)
        return r

    def hasNext(self) -> bool:
        return True if self.i < len(self.charset) - self.n + 1 else False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()