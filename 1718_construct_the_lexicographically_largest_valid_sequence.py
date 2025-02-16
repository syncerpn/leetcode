# greedy, but to make it lexico largest, better start with the first position going down to the last one
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2*n-1
        d = set()
        v = set()
        ans = [0] * m
        def place(i):
            for k in range(n, 0, -1):
                if k not in v and i not in d and (k == 1 or (i + k < m and i + k not in d)):
                    v.add(k)
                    d.add(i)
                    ans[i] = k
                    if k != 1:
                        d.add(i+k)
                        ans[i+k] = k
                    
                    if len(v) == n:
                        return True

                    j = i+1
                    while j < len(ans):
                        if ans[j] == 0:
                            if place(j):
                                return True
                            break
                        j += 1
                    
                    v.discard(k)
                    d.discard(i)
                    ans[i] = 0
                    if k != 1:
                        d.discard(i+k)
                        ans[i+k] = 0
            return False
        
        place(0)
        return ans