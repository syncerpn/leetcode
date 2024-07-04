# we keep track of difference between number of unique chars of left and right substring
# use a single O(n) mem to do that
# and a set to keep track of unique characters
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        d = set()
        a = 0

        lr_diff = [0] * (n+1)
        for i, c in enumerate(s):
            d.add(c)
            lr_diff[i+1] = len(d)

        d = set()
        for i, c in enumerate(s[::-1]):
            d.add(c)
            j = n-1-i
            lr_diff[j] -= len(d)
            if lr_diff[j] == 0:
                a += 1
            elif lr_diff[j] < 0:
                break
        return a
