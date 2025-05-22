# this was my solution, but wrong
# my thought was that, we can sort the query, first by the starting point, then by how large it expands
# then iterate nums, if a num needs to be reduced to zero, iterate the queries to find any query whose range contains num
# and remove those we dont need
# the idea was ofcourse not the optimal way
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        m = len(queries)
        n = len(nums)

        queries.sort(key=lambda q: (q[0], -q[1]))
        dp = [0] * (n + 1)

        i, j, k, s = 0, 0, 0, 0
        while i < n:
            if s + dp[i] >= nums[i]:
                s += dp[i]
                i += 1
            else:
                if j == m:
                    return -1
                a, b = queries[j]
                if a > i:
                    return -1
                if b >= i:
                    dp[i] += 1
                    dp[b+1] -= 1
                    k += 1
                j += 1
            
        return len(queries) - k

# use lee's solution and explanation again, because it is just beautiful
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries = sorted(queries)[::-1]
        ava = SortedList()
        cur = SortedList()
        for i in range(len(nums)):
            # we build a list of all remaining queries that may zero out the current num
            while queries and queries[-1][0] <= i:
                ava.add(queries.pop()[1])

            # also remove those that affected previous num, but not the current num
            while cur and cur[0] < i:
                cur.pop(0)

            # we transfer those from ava to cur until there are enough to zero out num
            while nums[i] > len(cur):
                if not ava or ava[-1] < i:
                    return -1
                cur.add(ava.pop())
        return len(ava)