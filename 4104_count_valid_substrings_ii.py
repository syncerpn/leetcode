# nice prob
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l = 0
        n = len(s)
        a = deque()
        b = -1
        ans = 0
        for r, c in enumerate(s):
            if c == "a":
                a.append(r)
            elif c == "b" and a:
                a = deque([a[-1]])
                if b < a[-1]:
                    b = r
            elif c == "c" and b > 0:
                while a and a[0] < b:
                    l = a.popleft() + 1
                b = -1
            ans += r - l + 1
        return ans

# beautiful solution
# where
# a: largest starting index of "a"
# b: largest starting index of "ab"
# c: largest starting index of "abc"
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        a = b = c = -1
        ans = 0
        for i, v in enumerate(s):
            if v == 'a':
                a = i
            elif v == 'b':
                b = a
            else:
                c = b
            ans += i - c
        return ans