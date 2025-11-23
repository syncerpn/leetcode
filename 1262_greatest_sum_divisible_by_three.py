# greedy, check the sum of all elements
# depending on the mod value
# if sum % 3 == 1, remove 1 smallest element that also % 3 == 1, or 2 smallest elements that % 3 == 2
# if sum % 3 == 2, remove 1 smallest element that also % 3 == 2, or 2 smallest elements that % 3 == 1
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        A = []
        B = []
        ans = 0
        for a in nums:
            ans += a
            if a % 3 == 1:
                A.append(a)
            elif a % 3 == 2:
                B.append(a)
        
        A.sort()
        B.sort()
        if ans % 3 == 1:
            m = float("inf")
            if len(A) > 0:
                m = A[0]
            if len(B) > 1:
                m = min(m, B[0] + B[1])
            ans -= m
        elif ans % 3 == 2:
            m = float("inf")
            if len(B) > 0:
                m = B[0]
            if len(A) > 1:
                m = min(m, A[0] + A[1])
            ans -= m
        return ans

# dp is also possible