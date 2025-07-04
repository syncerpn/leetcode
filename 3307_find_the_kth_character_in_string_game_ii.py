# duplicate or next-duplicate
# it shapes like a tree
# we find the root the k-th character (or k-1 index)
# and check how it changes after every operation
# beautifully, it all encodes in the bits of k-1
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        d = {a: b for a, b in pairwise("abcdefghijklmnopqrstuvwxyza")}
        k -= 1
        ans = "a"
        for a in operations:
            if k == 0:
                break
            if k & 1:
                ans = d[ans] if a else ans
            k >>= 1
        
        return ans