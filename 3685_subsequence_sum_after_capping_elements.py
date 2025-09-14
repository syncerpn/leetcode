# this was accepted during the contest lol
# not sure how it will end up in the end
# point is, for every value x, we make it knapsack problem
# constructing all possible sums from elements in nums with values up to x
# we can check whether k can be achieved by checking the difference between one of those sums, d, to k
# so that we can add x to that sum
# meaning that k - d must be divisible by x and we have enough x to add to d
# complexity should be O(n * k), but again, very specific implementation may cause problems
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        nums.sort()
        dp = set([0])
        l = 0
        ans = []
        for x in range(1, n+1):
            r = bisect.bisect(nums, x)
            for i in range(l, r):
                dp_next = set()
                for s in dp:
                    dp_next.add(s)
                    if s + nums[i] <= k:
                        dp_next.add(s + nums[i])
                dp = dp_next
            for d in dp:
                if (k - d) % x == 0 and (k - d) // x <= n - r:
                    ans.append(True)
                    break
            else:
                ans.append(False)
            
            l = r
        return ans