# this problem touches mono queue, or ordered set, or similar things
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # we are going to bound the range with two index pointers, l and r
        qmax = deque() # track the max value in index range (l, r)
        qmin = deque() # track the max value in index range (l, r)
        l = 0
        max_len = 0
        for r, n in enumerate(nums):
            # make sure it is monotonic decreasing
            while qmax and nums[qmax[-1]] <= n:
                qmax.pop()
            qmax.append(r)
            
            # while this one is monotonic increasing
            while qmin and nums[qmin[-1]] >= n:
                qmin.pop()
            qmin.append(r)
            
            # so now, we check whether the diff is within the limit
            # diff should be equal to max value - min value, no doubt
            # if diff is out of range, we need to tighten the range
            # by increasing l pointer
            while nums[qmax[0]] - nums[qmin[0]] > limit:
                l += 1
                # as l is updated, we now have a new index range (l_new, r)
                # with that in mind, max value of the range (l_new, r) may also change
                # we make sure that value is valid by trimming away all out-range values
                # simply by popping the very first out of the queue
                if qmax[0] < l:
                    qmax.popleft()
                
                # the same scenario may happen to min value as well
                # so we would do the similar thing, but with qmin
                if qmin[0] < l:
                    qmin.popleft()
            
            # when the condition is satisfied, we can calculate the new valid range
            # and keep track of the max length of the valid contiguous subarray
            max_len = max(max_len, r - l + 1)
        
        return max_len