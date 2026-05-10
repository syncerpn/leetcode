# obviously i can solve it
# maybe it is not 2100 rating
P = set(list(range(2, 1000000)))
for a in range(2, 1001):
    if a not in P:
        continue
    for b in range(a * a, 1000000, a):
        P.discard(b)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n, m = len(nums), max(nums)
        v = [False] * n
        d = defaultdict(list)
        for i, a in enumerate(nums):
            d[a].append(i)
        s = deque([(0, 0)])
        v[0] = True
        vp = set()

        while s:
            i, t = s.popleft()
            a = nums[i]
            if i == n - 1:
                return t
            if i > 0 and not v[i-1]:
                v[i-1] = True
                s.append((i-1, t+1))
            if not v[i+1]:
                v[i+1] = True
                s.append((i+1, t+1))
            
            if a in P and a not in vp:
                for b in range(a, m+1, a):
                    if b in d:
                        for j in d[b]:
                            if not v[j]:
                                s.append((j, t+1))
                                v[j] = True
                vp.add(a)
        
        return -1

# another way without vp
P = set(list(range(2, 1000000)))
for a in range(2, 1001):
    if a not in P:
        continue
    for b in range(a * a, 1000000, a):
        P.discard(b)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n, m = len(nums), max(nums)
        v = [False] * n
        d = defaultdict(list)
        for i in range(n-1, -1, -1):
            d[nums[i]].append(i)
        s = deque([(0, 0)])
        v[0] = True

        while s:
            i, t = s.popleft()
            a = nums[i]
            if i == n - 1:
                return t
            if i > 0 and not v[i-1]:
                v[i-1] = True
                s.append((i-1, t+1))
            if not v[i+1]:
                v[i+1] = True
                s.append((i+1, t+1))
            
            if a in P:
                for b in range(a, m+1, a):
                    if b in d:
                        for j in d[b]:
                            if not v[j]:
                                s.append((j, t+1))
                                v[j] = True
                        del d[b]
        
        return -1

# is this really a bit faster?
P = [False] * 1000001
P[0] = True
P[1] = True
for a in range(2, 1001):
    if P[a]:
        continue
    for b in range(a * a, 1000000, a):
        P[b] = True

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n, m = len(nums), max(nums)
        v = [False] * n
        d = defaultdict(list)
        for i in range(n-1, -1, -1):
            d[nums[i]].append(i)
        s = deque([(0, 0)])
        v[0] = True

        while s:
            i, t = s.popleft()
            a = nums[i]
            if i == n - 1:
                return t
            if i > 0 and not v[i-1]:
                v[i-1] = True
                s.append((i-1, t+1))
            if not v[i+1]:
                v[i+1] = True
                s.append((i+1, t+1))
            
            if not P[a]:
                for b in range(a, m+1, a):
                    if b in d:
                        for j in d[b]:
                            if not v[j]:
                                s.append((j, t+1))
                                v[j] = True
                        del d[b]
        
        return -1