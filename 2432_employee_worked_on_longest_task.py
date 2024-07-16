# track the longest task and worker id
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        w = logs[0][0]
        t = 0
        d = 0
        for i, k in logs:
            if d < k - t:
                d = k - t
                w = i
            elif d == k - t:
                w = min(w, i)
            t = k
        
        return w
