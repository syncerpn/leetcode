# the problem can be solve in O(nlogn) with sorting
# but it can even be better
# this solution is the most general one applying quick-select
# lets not care about space this time, because inplace swapping can be easily implemented on top of this
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we keep filtering out some values in nums until we found kth
        while nums:
            l = []
            r = []
            m = 0

            # choose a random pivot is better than fixed one
            pivot = random.choice(nums)
            
            # now do partitioning
            for n in nums:
                if n > pivot:
                    r.append(n)
                elif n < pivot:
                    l.append(n)
                else:
                    m += 1
            
            # and then detect which partition to be considered next
            if len(r) < k <= len(r) + m:
                return pivot
            elif len(r) >= k:
                nums = r
            else:
                nums = l
                k -= m + len(r)

# the following solution is quite similar to the above
# but some imply that median of median is better for choosing pivot
# im not sure though
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while nums:
            if k == len(nums):
                return min(nums)
            if k == 1:
                return max(nums)
            r = []
            l = []
            m = 0
            pivot = 0
            if len(nums) < 3:
                pivot = random.choice(nums)
            else:
                pivot = sorted([nums[0], nums[len(nums) // 2], nums[-1]])[1]
            
            for n in nums:
                if n > pivot:
                    r.append(n)
                elif n < pivot:
                    l.append(n)
                else:
                    m += 1
            
            if len(r) < k <= len(r) + m:
                return pivot
            elif len(r) >= k:
                nums = r
            else:
                nums = l
                k -= m + len(r)

# k-size heap is also good (nlogk)
# we try to maintain a heap of size k
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for n in nums[k:]:
            if n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, n)
        
        return h[0]