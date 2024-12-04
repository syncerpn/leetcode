# two pointer, greedy
# fairly easy
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        K = "abcdefghijklmnopqrstuvwxyz"
        V = "bcdefghijklmnopqrstuvwxyza"
        d = {a: b for a, b in zip(K, V)}
        i = 0
        for a in str1:
            if str2[i] == a or str2[i] == d[a]:
                i += 1
                if i == len(str2):
                    return True
        return False