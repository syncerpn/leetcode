# surprised this works
# what i concerned was the query queuing list
# but when looking back, its complexity is not that big
# lol, solved it myself
class StreamChecker:

    def __init__(self, words: List[str]):
        self.r = {}
        for word in words:
            n = self.r
            for c in word:
                if c not in n:
                    n[c] = {}
                n = n[c]
            n["."] = True

        self.q = []

    def query(self, letter: str) -> bool:
        q_next = []
        found = False
        if letter in self.r:
            qi_next = self.r[letter]
            q_next.append(qi_next)
            if "." in qi_next:
                found = True
        
        for qi in self.q:
            if letter in qi:
                qi_next = qi[letter]
                q_next.append(qi_next)
                if "." in qi_next:
                    found = True
        
        self.q = q_next
        return found

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)