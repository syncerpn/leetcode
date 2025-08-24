# prefix max and suffix min
# kinda like dp
# we wanna jump directly to the max from the left
# or jump to the far-est to the right and then jump to the max from the left of the new position
# so, just determine right to left
# which one is the max
# indirect jump can use this information if a right jump is needed
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [0] * n
        s = [0] * n
        ans = [0] * n

        p[0] = nums[0]
        for i in range(1, n):
            p[i] = max(nums[i], p[i-1])
        
        s[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            s[i] = min(nums[i], s[i+1])
        
        ans[n-1] = p[n-1]
        for i in range(n-2, -1, -1):
            ans[i] = p[i]
            if p[i] > s[i+1]:
                ans[i] = max(ans[i], ans[i+1])
        
        return ans

# the problem can be solved as graph
# flip i and j in the second condition
# then the statement reads:
# jump i to j if i < j and A[i] > A[j]
# jump j to i if i < j and A[i] > A[j]
# therefore, every inversion is an undirected edge, and vice versa
# let S[i] = min(A[i], A[i+1], ..., A[N-1])
# consider a connected component C touching i with maximum reachable value m
# if m <= S[i+1], then no edge from C to {i+1, ..., N-1} is possible, so we have exhausted our search (there are no more outgoing edges from C to consider.)
# also, connected components must be intervals: when a component [i..j] grows to include the lowest k > j + 1 possible, then the nodes [j+1..k-1] in between must have larger values than A[k] by construction, and therefore included.
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = nums[:]
        for i in range(n-2, -1, -1):
            s[i] = min(s[i], s[i+1])
        
        ans = []
        m = 0
        for i, a in enumerate(nums):
            m = max(m, a)
            if i == n - 1 or m <= s[i+1]:
                ans += [m] * (i + 1 - len(ans))
                m = 0
        
        return ans

# also thought of a union-find for a graph-like solution during the contest
# but i failed to implement it though