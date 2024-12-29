# greedy, longer should be better
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        m = 1 + n - numFriends
        ans = word[:m]
        for i, c in enumerate(word):
            if c > ans[0]:
                ans = word[i:min(n, i+m)]
            elif c == ans[0]:
                ans = max(ans, word[i:min(n, i+m)])
        return ans