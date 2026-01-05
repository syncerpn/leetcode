# permutations
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        return sorted([(t, l, r, b) for t, l, r, b in permutations(words, 4) if t[0] == l[0] and t[3] == r[0] and b[0] == l[3] and b[3] == r[3]])

# backtrack with early stopping
# list(v) is necessary to avoid changing set size/content during loop
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        def backtrack(s, v):
            if len(s) == 4:
                if s[3][0] == s[1][3] and s[3][3] == s[2][3]:
                    ans.append(s[:])
            else:
                valid = True
                if len(s) == 3:
                    if s[0][3] != s[2][0]:
                        valid = False
                elif len(s) == 2:
                    if s[0][0] != s[1][0]:
                        valid = False
                if valid:
                    for w in list(v):
                        s.append(w)
                        v.discard(w)
                        backtrack(s, v)
                        v.add(w)
                        s.pop()
        backtrack([], set(words))
        return sorted(ans, key=lambda s: tuple(s))