# general problem for partitioning
# some others are duplicate of this one
# the key point is to partition into k buckets from largest to smallest
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        a = sum(nums) // k
        b = [0] * k
        def dfs(i):
            if i == len(nums):
                return len(set(b)) == 1
            for j in range(k):
                b[j] += nums[i]
                if b[j] <= a and dfs(i+1):
                    return True
                b[j] -= nums[i]
                if b[j] == 0:
                    break
            return False
        return dfs(0)