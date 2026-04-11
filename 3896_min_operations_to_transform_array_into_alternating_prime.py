# prime sieve
# no precomputed
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        P = [True] * 100004
        P[0] = False
        P[1] = False
        for i in range(2, 317):
            if not P[i]:
                continue
            
            j = i
            while i * j < len(P):
                P[i * j] = False
                j += 1

        while not P[-1]:
            P.pop()

        Q = [0] * len(P)
        p = len(P) - 1
        for i in range(len(P)-1, -1, -1):
            if P[i]:
                p = i
            Q[i] = p - i

        ans = 0
        for i, a in enumerate(nums):
            if i % 2:
                if Q[a] == 0:
                    ans += 2 if a == 2 else 1
            else:
                ans += Q[a]
        return ans

# binary search is also fine
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        P = [True] * 100004
        for i in range(2, 317):
            if not P[i]:
                continue
            
            j = i
            while i * j < len(P):
                P[i * j] = False
                j += 1
        Q = []
        for i in range(2, len(P)):
            if P[i]:
                Q.append(i)
        ans = 0
        for i, a in enumerate(nums):
            j = bisect.bisect_left(Q, a)
            if i % 2:
                if a == 2:
                    ans += 2
                elif a == Q[j]:
                    ans += 1
            else:
                if a != Q[j]:
                    ans += Q[j] - a
        return ans

# precomputed feels like cheating lol
class Solution:
    P = [True] * 100004
    P[0] = False
    P[1] = False
    for i in range(2, 317):
        if not P[i]:
            continue
        
        j = i
        while i * j < len(P):
            P[i * j] = False
            j += 1

    while not P[-1]:
        P.pop()

    Q = [0] * len(P)
    p = len(P) - 1
    for i in range(len(P)-1, -1, -1):
        if P[i]:
            p = i
        Q[i] = p - i

    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i, a in enumerate(nums):
            if i % 2:
                if Solution.Q[a] == 0:
                    ans += 2 if a == 2 else 1
            else:
                ans += Solution.Q[a]
        return ans