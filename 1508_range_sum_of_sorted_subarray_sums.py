# similar to merge k sorted list
# we start with prefix sum of each element at each index in nums
# then use heapq to sort them into a list
# when popped, add the next prefix sum the popped prefix sum into the list if there is one
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        h = []
        ans = 0
        for i in range(n):
            heapq.heappush(h, (nums[i], i))
        for k in range(right):
            p, i = heapq.heappop(h)
            if k >= left - 1:
                ans = (ans + p) % MOD
            if i + 1 < n:
                heapq.heappush(h, (p + nums[i+1], i+1))
        return ans

# crazy O(n) time solution from lee215
# pretty difficult to understand though
# wonder how someone could come up with this
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        B, C = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + nums[i]
            C[i + 1] = C[i] + B[i + 1]

        # original array: A
        # B[i] = sum(A[:i]) = A[0] + A[1] + ... + A[i-1] (for i>=1)
        # C[i] = sum(B[:i+1]) = B[0] + B[1] + ... + B[i] (for i>=1)


        def count_sum_under(score):
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
                res += j - i
            return res        
            # i is the smallest number s.t. 
            # sum(A[i:j]) = sum(A[:j]) - sum(A[:i]) = B[j] - B[i] <= score
            # Then all subarrays which ends with A[j-1] and sums <= score
            # are all subarrays which ends with A[j-1] and starts from or after A[i].
            # So the number of them is j - i.

        def sum_k_sums(k):
            score = kth_score(k)
            # Use kth_score function to find score: the kth sum in sorted subarray sums 
            # What's left is to add up all subarray sums that <= score
            res = i = 0
            for j in range(n + 1):
                while B[j] - B[i] > score:
                    i += 1
            # For each j, find i which is the smallest number s.t. sum(A[i:j]) <= score
                res += B[j] * (j - i + 1) - (C[j] - (C[i - 1] if i else 0))
            # this is equal to:
            # for m in range(i, j): res += sum(A[m:j]) = B[j] - B[m]   
            # sum_m(B[j] - B[m]) = B[j]*(j-i+1) - (B[i] + B[i+1] + ... + B[j]) 
            # B[i] + B[i+1] + ... + B[j] = (B[0] + B[1] + ... +B[j]) - (B[0] + B[1] + ... +B[i-1])
            # = C[j] - (C[i-1] if i else 0))
            return res - (count_sum_under(score) - k) * score
            # There may exists multiple subarray sums equal to score

        def kth_score(k):
            l, r = 0, B[n]
            while l < r:
                m = (l + r) // 2
                if count_sum_under(m) < k:
                    l += 1
                    l = m + 1
                else:
                    r = m
            return l
            # with count_sum_under function, this is just regular binary search.
            # The subarray sum is positive and at most sum(A[:]) = B[n]

        return (sum_k_sums(right) - sum_k_sums(left - 1))%(10**9+7)