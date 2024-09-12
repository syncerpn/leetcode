# with heapq, not very efficient
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = []
        ans = []
        for i, n in enumerate(nums):
            heapq.heappush(s, (-n, i))
            if i >= k-1:
                m, j = heapq.heappop(s)
                while i - j > k - 1:
                    m, j = heapq.heappop(s)

                ans.append(-m)
                heapq.heappush(s, (m, j))
        return ans

# monostack decreasing
# we build such stack to keep track of the maximum of a sliding window
# the current element need to be in the stack all the time
# to do so, we remove all element in the stack that is smaller than the current one
# as the leftmost element is out of the window
# remove it from the stack as well
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        j = 0
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)

            if j > q[0]:
                q.popleft()
            
            if i >= k - 1:
                ans.append(nums[q[0]])
                j += 1
        
        return ans