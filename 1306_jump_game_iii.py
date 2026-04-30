# just graph navigation is enough
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        v = [False] * n
        v[start] = True
        s = [start]
        while s:
            i = s.pop()
            a = arr[i]
            if a == 0:
                return True
            if i - a >= 0 and not v[i-a]:
                s.append(i-a)
                v[i-a] = True
            if i + a <  n and not v[i+a]:
                s.append(i+a)
                v[i+a] = True
        return False

# union-find may look fit, yet wont work
# because the graph is actually directed
# meaning that you may go a to b but may not go b to a