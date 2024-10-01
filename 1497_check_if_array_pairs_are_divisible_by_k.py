# counting
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k:
            return False
        d = Counter([a % k for a in arr])
        for i in range(1, k//2+1):
            if d[i] != d[k-i]:
                return False
        return d[0] % 2 == 0