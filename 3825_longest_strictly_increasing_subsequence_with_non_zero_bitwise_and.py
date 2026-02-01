# combined of longest increasing subsequence and array bitwise and
# we just need to filter bit position first
# then count the length
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def longest_subsequence(A):
            s = []
            for a in A:
                if not s or a > s[-1]:
                    s.append(a)
                else:
                    s[bisect.bisect_left(s, a)] = a
            return len(s)

        ans = 0
        for b in range(32):
            A = []
            for a in nums:
                if (a >> b) & 1:
                    A.append(a)
            ans = max(ans, longest_subsequence(A))
        return ans