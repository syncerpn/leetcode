# counting and hashing every two-op product
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        ans = 0
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                p = a * b
                if p not in d:
                    d[p] = 1
                else:
                    d[p] += 1
        return 8 * sum(d[p] * (d[p] - 1) // 2 for p in d)