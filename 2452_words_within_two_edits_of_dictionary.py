# given constraints allowed brute-force
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for a in queries:
            for b in dictionary:
                t = 0
                for c, d in zip(a, b):
                    if c != d:
                        t += 1
                    if t > 2:
                        break
                else:
                    ans.append(a)
                    break
        return ans

# can be solved with trie anyway