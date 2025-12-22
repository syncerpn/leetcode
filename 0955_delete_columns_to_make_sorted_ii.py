# my solution is like optimal in both theory and runtime
# iterate columns, tracking range of equal adjacent chars
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = list(zip(*strs))
        m, n = len(strs), len(strs[0])
        d = [[0, n-1]]
        ans = 0
        k = 0
        while d and k < m:
            d_next = []
            for l, r in d:
                d_next.append([l, l])
                for i in range(l, r):
                    if strs[k][i] > strs[k][i+1]:
                        ans += 1
                        break
                    elif strs[k][i] == strs[k][i+1]:
                        d_next[-1][-1] += 1
                    else:
                        if d_next[-1][0] == d_next[-1][1]:
                            d_next.pop()
                        d_next.append([i+1, i+1])
                else:
                    if d_next[-1][0] == d_next[-1][1]:
                        d_next.pop()
                    continue
                break
            else:
                d = d_next
            k += 1
        return ans