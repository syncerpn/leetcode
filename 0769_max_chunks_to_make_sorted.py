# turned out, we just need to make max of A[0] to A[i] equals to i
# then makes it one chunk
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m, ans = 0, 0
        for i, n in enumerate(arr):
            m = max(m, n)
            if m == i:
                ans += 1
        return ans

# if the input is not [0, n-1] but random numbers
# we can compare max of A[0] to A[i] to sorted(A)[i]