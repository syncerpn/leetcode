# recursively partition substrings of s
class Solution:
    cache = {}
    def partition(self, s: str) -> List[List[str]]:
        if s in Solution.cache:
            return Solution.cache[s]
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        Solution.cache[s] = ans
        return ans
        