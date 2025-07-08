# dp + binary search
# should start asking chatgpt from now on to learn the thought process
# for this one the thought process suggested by chatgpt is that
# we want to use dp with the meaning
# dp[i][j] = max value for attending at most j events out of the first i events
# we will first sort the events by their end date
# iterate the event list
# try to find the last event (j) that ends before the current event (i) (start of event i > end of event j)
# then check the highest value we can obtain by either attend the current event i or not attend it
# also, bisect left the better than bisect right, so that we can have strict start of event i > end of event j (must be >, not >= condition)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            a, b, v = events[i-1]
            for j in range(1, k + 1):
                # if we skip the event i
                dp[i][j] = dp[i-1][j]

                # or we attend the event i
                idx = bisect.bisect_left(events, a, key=lambda x: x[1])
                dp[i][j] = max(dp[i][j], dp[idx][j-1] + v)
        
        return max(dp[n])

# faster and smaller by caching last non-overlapping event instead of binary search every time
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        events_start_sorted = sorted([(a, i) for i, (a, _, _) in enumerate(events)])

        last_non_overlapping = [-1] * n
        j = 0
        for a, i in events_start_sorted:
            while events[j][1] < a:
                j += 1
            last_non_overlapping[i] = j - 1
        
        dp = [0] * n
        ans = 0

        for j in range(1, k + 1):
            max_value = -1
            dp_next = [-1] * n
            for i in range(n):
                if j == 1:
                    max_value = max(max_value, events[i][2])
                elif last_non_overlapping[i] >= 0 and dp[last_non_overlapping[i]] >= 0:
                    max_value = max(max_value, dp[last_non_overlapping[i]] + events[i][2])
                dp_next[i] = max_value
            dp = dp_next
            ans = max(ans, max_value)
        return ans