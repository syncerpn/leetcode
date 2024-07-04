# google online assessment?
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


# we keep track of the first and last appearance of each character in s
# as string is split, this information tells how many unique chars in left and right substring
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        first = {}
        last = {}
        
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # we sort the combination of first and last indices of each unique character
        indices = list(first.values()) + list(last.values())
        indices.sort()
        
        # once we reach the middle of the sorted list, it is guaranteed that the number of unique chars in left and right are the same
        # so the pair of median of the sorted list tells the starting point of the split and its end point
        m = len(indices)//2
        
        return indices[m] - indices[m-1]
# this is the math proof the above solution
# if we have a total of m unique chars, then indices should have 2 * m elements
# remind that we split in the middle in indices
# so lets assume that the left has k chars that do not appear in the right and i chars in common with the right
# we know that i + 2 * k = m
# the right one should have i common chars and m - i - k chars that do not appear in the left
# m - i - k = i + 2 * k - i - k = k
# so the number of unique chars in the left and right are the same: i + k == i + k