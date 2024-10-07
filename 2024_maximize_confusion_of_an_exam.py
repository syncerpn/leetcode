# naive sliding window
# with maximum k outliners
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        for r in "TF":
            l, t = 0, 0
            for i, c in enumerate(answerKey):
                if c != r:
                    t += 1
                while t > k:
                    if answerKey[l] != r:
                        t -= 1
                    l += 1
                ans = max(ans, i-l+1)
        
        return ans

# much better single pass
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t, f = 0, 0
        l = 0
        for c in answerKey:
            if c == "T":
                t += 1
            else:
                f += 1
            if t > k and f > k:
                if answerKey[l] == "T":
                    t -= 1
                else:
                    f -= 1
                l += 1
        return len(answerKey) - l