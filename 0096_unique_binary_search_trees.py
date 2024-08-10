# backtracking with memoi
class Solution:
    def numTrees(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        def make_tree(k):
            if k in cache:
                return cache[k]
            ans = 0
            for i in range(k):
                ans += make_tree(i) * make_tree(k-i-1)
            cache[k] = ans
            return cache[k]
        return make_tree(n)

# or we could make it into dp
# same formula though