# my initial thought on this
# first, solve it the same way as the previous problem with k=1
# second, for each event, we can find the gap that is big enough to move this event to that gap
# that gap should not be right before or right after the event
# use binary search on sorted gap and index-check the condition is the way
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)

        gaps = [(startTime[i] - endTime[i-1], i) for i in range(n+1)]
        ans = max([a[0] + b[0] for a, b in pairwise(gaps)])
        
        sorted_gaps = sorted(gaps)
        for i in range(n):
            j = bisect.bisect_left(sorted_gaps, endTime[i] - startTime[i], key=lambda x: x[0])
            while j <= n:
                if i == sorted_gaps[j][1] or i == sorted_gaps[j][1] - 1:
                    j += 1
                else:
                    break
            else:
                continue
            ans = max(ans, gaps[i][0] + gaps[i+1][0] + endTime[i] - startTime[i])

        return ans

# similar idea, but reduce time complexity of binary search and sorting
# by checking prefix and suffix max gaps, not right before or right after, for each event
# if that max gap exist for an event, we can move the event to that gap
# and the free time now = two consecutive gaps + the event duration
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)

        gaps = [startTime[i] - endTime[i-1] for i in range(n+1)]
        prefix, suffix = [0], [0]
        for i in range(n-1):
            prefix.append(max(prefix[-1], gaps[i]))
            suffix.append(max(suffix[-1], gaps[~i]))

        ans = max([a + b for a, b in pairwise(gaps)])
        for i in range(n):
            d = endTime[i] - startTime[i]
            if prefix[i] >= d or suffix[~i] >= d:
                ans = max(ans, d + gaps[i] + gaps[i+1])

        return ans

# further optimize a bit, removing prefix for less space, and combine max checking for answer
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)

        gaps = [startTime[i] - endTime[i-1] for i in range(n+1)]
        suffix = [0]
        for i in range(n-1):
            suffix.append(max(suffix[-1], gaps[~i]))

        ans = 0
        p = 0
        for i in range(n):
            d = endTime[i] - startTime[i]
            if p >= d or suffix[~i] >= d:
                ans = max(ans, d + gaps[i] + gaps[i+1])
            else:
                ans = max(ans, gaps[i] + gaps[i+1])
            p = max(p, gaps[i])

        return ans