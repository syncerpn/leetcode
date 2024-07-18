# more general than #2935 and #2932
# use trie as those two with simplification
# because the constraints do not require sliding window and removing trie element
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie_root = {}
        B = 31

        def add(n):
            node = trie_root
            b = B
            while b >= 0:
                p = (n >> b) & 1
                if p not in node:
                    node[p] = {}
                node = node[p]
                b -= 1

        def find_xor_max_counterpart(n):
            node = trie_root
            b = B
            m = 0
            while b >= 0:
                p = (n >> b) & 1
                if 1-p in node:
                    p = 1-p
                m |= p << b
                node = node[p]
                b -= 1
            return m

        nums.sort()
        x = 0
        for n in nums:
            add(n)
            m = find_xor_max_counterpart(n)
            x = max(x, m ^ n)
        
        return x

# following answer actually build the result instead of search for a pair
# which is very creative and beautiful
# copied from others
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer