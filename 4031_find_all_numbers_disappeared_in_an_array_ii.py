# append the bound to make it easy to implement
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.append(lower - 1)
        nums.append(upper + 1)
        nums.sort()
        ans = []
        for a, b in pairwise(nums):
            if a < lower - 1:
                continue
            if b > upper + 1:
                break
            
            l, r = a + 1, b - 1
            if l > r:
                continue
            ans.append([l, r])
        return ans