# dp solution is trivial
class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = [1, 1, 1, 1, 1]
        for _ in range(n-1):
            for i in range(1, 5):
                ans[i] = ans[i] + ans[i-1]
        
        return sum(ans)

# or math-based with combination
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24