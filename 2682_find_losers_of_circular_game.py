# seems like no better way than simulation
# set can be used
# but may be bit array is better for space
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        if n == 1:
            return []

        t = [False] * n
        t[1] = True
        i = 1
        m = 1
        while True:
            i = (i + m * k) % n
            if t[i]:
                break
            t[i] = True
            m += 1
        r = t.append(t[0])
        t[0] = True
        return [i for i in range(n+1) if not t[i]]

# set solution
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        s = set(list(range(2, n+1)))
        for m in range(1, n+1):
            i = (m * (m + 1) * k // 2) % n + 1
            if i not in s:
                return s
            s.discard(i)
        return []