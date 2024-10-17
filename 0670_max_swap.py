# greedy, try to make the very first digit as big as possible
# and by swapping the latest possible digit with it
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [c for c in str(num)]
        ss = sorted(s, reverse=True)
        for i in range(len(s)):
            a, b = s[i], ss[i]
            if a != b:
                x, y = a, b
                for j in range(len(s)-1,-1,-1):
                    if s[j] == b:
                        s[j] = a
                        break
                s[i] = b
                break
        return int("".join(s))
