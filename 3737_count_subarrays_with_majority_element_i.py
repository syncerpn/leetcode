# brute-force O(n2) is default
# using prefix-sum
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = [0]
        for a in nums:
            P.append(P[-1] + int(a == target))
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if j - i < (P[j] - P[i]) * 2:
                    ans += 1
        return ans

# O(n) solution just like #3739
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = [1] + [0] * (n + n + 2)
        acc = [1] + [0] * (n + n + 2)
        ans = p = 0
        for a in nums:
            p += 1 if a == target else -1
            count[p] += 1
            acc[p] = acc[p-1] + count[p]
            ans += acc[p-1]
        return ans
        