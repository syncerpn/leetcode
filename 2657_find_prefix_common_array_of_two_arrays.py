# use set, or count array
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sA, sB = set(), set()
        n = len(A)
        ans = [0] * n
        c = 0
        for i in range(n):
            a, b = A[i], B[i]
            sA.add(a)
            sB.add(b)
            if a == b:
                c += 1
            else:
                if a in sB:
                    c += 1
                if b in sA:
                    c += 1
            ans[i] = c
        return ans