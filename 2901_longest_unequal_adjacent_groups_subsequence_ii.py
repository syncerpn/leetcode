# dp O(n2)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(a, b):
            if len(a) != len(b):
                return False
            return sum(i != j for i, j in zip(a, b)) == 1
        
        dp = [1] * len(words)
        dq = [[s] for s in words]
        m = 0
        for i, (s, g) in enumerate(zip(words, groups)):
            for j in range(i):
                r, k = words[j], groups[j]
                if k != g and check(s, r):
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        dq[i] = dq[j] + [s]
                if dp[i] > dp[m]:
                    m = i
        
        return dq[m]

# space optimized version, where we save the jump to trace back
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(a, b):
            if len(a) != len(b):
                return False
            return sum(i != j for i, j in zip(a, b)) == 1
        
        dp = [1] * len(words)
        dq = [0] * len(words)
        m = 0
        for i, (s, g) in enumerate(zip(words, groups)):
            for j in range(i):
                r, k = words[j], groups[j]
                if k != g and check(s, r):
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        dq[i] = j - i
                if dp[i] > dp[m]:
                    m = i
        ans = [words[m]]
        while dq[m] != 0:
            m += dq[m]
            ans.append(words[m])
        return ans[::-1]

# this is not the solution to the problem
# because i misunderstood the problem at first,
# but it leads to another quite fun problem
# that shares almost all the rules with the original problem
# but just that every pair of words in the answer
# must has hamming distance of 1
# lol
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        d = {}
        m, p, q = 0, 0, 0
        for i, (s, g) in enumerate(zip(words, groups)):
            l = len(s)
            if l not in d:
                d[l] = {}
            
            for j in range(l):
                r = s[:j] + " " + s[j+1:]
                if r not in d[l]:
                    d[l][r] = {}
                d[l][r][g] = i
                if len(d[l][r]) > m:
                    m = len(d[l][r])
                    p, q = l, r
        
        return [words[i] for i in sorted(list(d[p][q].values()))]