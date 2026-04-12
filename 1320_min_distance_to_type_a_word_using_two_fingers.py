# state mapping
class Solution:
    def minimumDistance(self, word: str) -> int:
        KEYPAD = {c: (i//6, i%6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        D = {(a + b): abs(KEYPAD[a][0] - KEYPAD[b][0]) + abs(KEYPAD[a][1] - KEYPAD[b][1]) for a in KEYPAD for b in KEYPAD}
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            D[" " + c] = 0
        n = len(word)
        word += " "
        S = {(-1, 0): 0}
        for s in range(1, n):
            S_next = {}
            for a, b in S:
                for c, d in [(s, b), (a, s)]:
                    if (c, d) not in S_next:
                        S_next[(c, d)] = inf
                    S_next[(c, d)] = min(S_next[(c, d)], S[(a, b)] + D[word[a] + word[c]] + D[word[b] + word[d]])
            S = S_next
        return min(S.values())

# same idea as above but more optimally implemented as dijkstra
class Solution:
    def minimumDistance(self, word: str) -> int:
        KEYPAD = {c: (i//6, i%6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        D = {(a + b): abs(KEYPAD[a][0] - KEYPAD[b][0]) + abs(KEYPAD[a][1] - KEYPAD[b][1]) for a in KEYPAD for b in KEYPAD}
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            D[" " + c] = 0
        n = len(word)
        word += " "
        h = [(0, 0, -1)]
        v = set()
        while h:
            c, a, b = heapq.heappop(h)
            if (a, b) in v:
                continue
            v.add((a, b))
            if max(a, b) == n - 1:
                return c
            d = max(a, b) + 1
            heapq.heappush(h, (c + D[word[a] + word[d]], d, b))
            heapq.heappush(h, (c + D[word[b] + word[d]], a, d))
        
        return -1

# also possible to implement as dp
# but the above state machine solution is much easier to understand
# the following solution is super well implemented for runtime
class Solution:
    def minimumDistance(self, word: str) -> int:
        KEYPAD = {c: (i//6, i%6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        D = {(a + b): abs(KEYPAD[a][0] - KEYPAD[b][0]) + abs(KEYPAD[a][1] - KEYPAD[b][1]) for a in KEYPAD for b in KEYPAD}

        n = len(word)
        dp = [0] * 26
        for c1, c2 in pairwise(word):
            c1_to_c2 = D[c1+c2]
            new_dp = [inf] * 26
            for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                c_to_c2 = D[c+c2]
                ci = ord(c) - ord("A")

                leave_on_c = c1_to_c2 + dp[ci]
                if leave_on_c < new_dp[ci]:
                    new_dp[ci] = leave_on_c
                
                leave_on_c1 = c_to_c2 + dp[ci]
                if leave_on_c1 < new_dp[ord(c1) - ord("A")]:
                    new_dp[ord(c1) - ord("A")] = leave_on_c1
            dp, new_dp = new_dp, dp
            new_dp.clear()
        
        return min(dp)