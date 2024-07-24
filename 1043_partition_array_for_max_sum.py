# could not solve this one
# so i copied solution from others to learn the new things
# it is dp
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # we create a dp to solve sub problem such that:
        # find the way to maximize partition sum up of array from beginning up to i
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            m = 0
            # subarray has length of at most k
            # we try k ways to partition it
            # and store the max sum
            # it becomes: max of:
            # current_value
            # or the solution up to i-j + the max or i-j up to i multiply with times it replaces others
            # which is j
            for j in range(1, min(k,i)+1):
                m = max(m, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + m*j)
        return dp[n]

# optimize for O(k) space
# because we only need to log upto k previous max sum
# we can allocate and use k-length array for dp memoi
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * k
        for i in range(1, n+1):
            m = 0
            s = 0
            for j in range(1, min(k,i)+1):
                m = max(m, arr[i-j])
                s = max(s, dp[(i-j)%k] + m*j)
            dp[i % k] = s
        return dp[n % k]