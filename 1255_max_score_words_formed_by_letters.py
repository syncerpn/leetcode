# backtracking
# typical hard problem, i guess
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(w):
            s = 0
            for c in w:
                s += score[ord(c) - ord("a")]
            return s
        
        def valid(S, B):
            for s, b in zip(S, B):
                if s > b:
                    return False
            return True

        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        words.sort(key=word_score)
        W = [[w.count(c) for c in ALPHABET] for w in words]

        B = [letters.count(c) for c in ALPHABET] # budget
        S = [sum(w) for w in zip(*W)] # current set
        V = [True] * len(W)
        ans = 0
        while any(V):
            if valid(S, B):
                ans = max(ans, sum(x * y for x, y in zip(S, score)))
            for i in range(len(V)):
                if V[i]:
                    V[i] = False
                    for j in range(len(S)):
                        S[j] -= W[i][j]
                    break
                else:
                    V[i] = True
                    for j in range(len(S)):
                        S[j] += W[i][j]

        return ans