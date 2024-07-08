# no other than O(n3) solution, lol
# i got overthinking after doing leetcode for quite some time
# O(n3) solution with early stopping
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        r = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                da = abs(arr[i] - arr[j])
                if da > a:
                    continue
                for k in range(j+1, n):
                    db = abs(arr[j] - arr[k])
                    dc = abs(arr[k] - arr[i])
                    if db <= b and dc <= c:
                        r += 1
        return r
