# quite easy
# for optimal solution, just keep track of only the dominant number
# no need for a dict of every value
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        c, x = max([(k, i) for i, k in Counter(nums).items()])
        k = 0
        for i, a in enumerate(nums):
            if a == x:
                k += 1
                c -= 1
                if k > (i + 1) // 2 and c > (n - i - 1) // 2:
                    return i
        
        return -1