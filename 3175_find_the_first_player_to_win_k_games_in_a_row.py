# simulate it
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        skills = deque([(i, s) for i, s in enumerate(skills)])
        k = min(k, len(skills) - 1)
        i, a = skills.popleft()
        m = 0
        while m < k:
            j, b = skills.popleft()
            if a > b:
                m += 1
                skills.append((j, b))
            else:
                m = 1
                skills.append((i, a))
                i, a = j, b
        return i

# or just no
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return skills.index(max(skills))
        i = 0
        m = 0
        for j in range(1, n):
            if skills[i] > skills[j]:
                m += 1
            else:
                i = j
                m = 1
            if m >= k:
                break
        return i