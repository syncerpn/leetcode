# backtrack for a general solution
# maybe we can also iterate and check every 3-digit num
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        v = set()
        d = Counter(digits)

        def backtrack(s):
            if len(s) == 3:
                if s[-1] % 2 == 0:
                    v.add(tuple(s))
            else:
                for c in d:
                    if not s and c == 0:
                        continue
                    if d[c] > 0:
                        d[c] -= 1
                        s.append(c)
                        backtrack(s)
                        s.pop()
                        d[c] += 1
        
        backtrack([])
        return len(v)