# bruteforce solution
# could have done this and get better rank in the contest
# but i was so greedy
# trying to solve both this and its harder version at the same time
# so ended up trying this at the very last minute
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        V = "aeiou"
        ans = 0
        n = len(word)

        for i in range(n):
            m = 0
            v = set(["a", "e", "i", "o", "u"])
            for j in range(i, n):
                if word[j] in V:
                    v.discard(word[j])
                else:
                    m += 1
                if m > k:
                    break
                if m == k and not v:
                    ans += 1
        return ans