# simulation solution
class Solution:
    def kthCharacter(self, k: int) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        D = {c: i for i, c in enumerate(A)}
        def next(s):
            return s + "".join([A[((D[c] + 1) % 26)] for c in s])
        
        s = "a"
        while len(s) < k:
            s = next(s)
        return s[k-1]

# but this more crazy lol
# by lee215 anyway
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k - 1).bit_count())