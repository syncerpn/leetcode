# kinda prefix sum
# good problem that took some time to figure out optimal solution
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        p = []
        for i, c in enumerate(boxes):
            if c == "1":
                p.append(i)
        k = len(p)
        ans = [sum(p)]
        j = 0
        for i in range(1, len(boxes)):
            # as we move to next box
            while j < k and p[j] < i:
                j += 1
            # all "1" on the right of current index i take one step back
            # and all "1" on the left take one step further
            # counted by k-j and j respectively
            ans.append(ans[-1] - (k-j) + j)
        return ans