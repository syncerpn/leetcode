# first, we want to move all k, no less
# second, we want to move k consecutive events the same direction, i.e. to the left or to the right does not matter
# finally, with these things, we can check the time slot, between the event ends before the first in k and the event starts after the last in k
# free time after rescheduling should equal to total free time in that slot
# just use sliding-window to calculate sum of all occupied time of those k events
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        s = 0
        ans = 0
        for i in range(n+1):
            if i >= k:
                if i == k:
                    l = 0
                else:
                    l = endTime[i-k-1]
                
                if i == n:
                    r = eventTime
                else:
                    r = startTime[i]
                
                ans = max(ans, r - l - s)
                s -= endTime[i-k] - startTime[i-k]
            if i < n:
                s += endTime[i] - startTime[i]
        return ans

# an easier way to think of it
# that is to merge k + 1 gaps between k consecutive events
# trick: append and use negative index for endTime
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)
        s = 0
        ans = 0
        for i in range(n+1):
            s += startTime[i] - endTime[i-1]
            if i >= k:
                ans = max(ans, s)
                s -= startTime[i-k] - endTime[i-k-1]

        return ans