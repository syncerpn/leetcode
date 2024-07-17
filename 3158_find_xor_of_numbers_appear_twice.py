# need set
# dont overthinking it
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s = set()
        x = 0
        for n in nums:
            if n in s:
                x ^= n
            s.add(n)
        return x
