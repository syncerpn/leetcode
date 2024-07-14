# good problem for practicing heapq and quick select
# obviously, we need k largest numbers
# heapq is pretty much trivial for experienced coders
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = []

        for i, n in enumerate(nums):
            heapq.heappush(h, (n, i))
            if i >= k:
                heapq.heappop(h)
        
        return [n[0] for n in sorted(h, key=lambda x: x[1])]

# or does k-largest trigger something?
# yes, its quick select
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pivot = 0
        nums_tmp = nums[:]
        # find k+1th largest instead
        k_tmp = k+1
        while nums_tmp:
            if k_tmp == len(nums_tmp):
                pivot = min(nums_tmp)
                break
            if k_tmp == 1:
                pivot = max(nums_tmp)
                break
            r = []
            l = []
            pivot, m = 0, 0
            if len(nums_tmp) < 3:
                pivot = random.choice(nums_tmp)
            else:
                pivot = sorted([nums_tmp[0], nums_tmp[len(nums_tmp) // 2], nums_tmp[-1]])[1]
            
            for n in nums_tmp:
                if n > pivot:
                    r.append(n)
                elif n < pivot:
                    l.append(n)
                else:
                    m += 1
            
            if len(r) < k_tmp <= len(r) + m:
                break
            elif len(r) >= k_tmp:
                nums_tmp = r
            else:
                nums_tmp = l
                k_tmp -= m + len(r)
        
        result = []
        gt = 0
        for n in nums:
            if n > pivot:
                gt += 1

        for n in nums:
            if n > pivot:
                result.append(n)
            elif n == pivot and k > gt:
                k -= 1
                result.append(n)
        return result