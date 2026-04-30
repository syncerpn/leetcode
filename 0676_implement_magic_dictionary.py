# every possible segment
class MagicDictionary:
    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def __init__(self):
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.count = collections.Counter(nei for word in dictionary
                                        for nei in self._genneighbors(word))


    def search(self, word: str) -> bool:
        return any(self.count[nei] > 1 or
                    self.count[nei] == 1 and word not in self.words
                    for nei in self._genneighbors(word))

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)