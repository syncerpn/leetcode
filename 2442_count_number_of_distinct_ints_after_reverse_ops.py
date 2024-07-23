# reverse with string conversion
# or with calculation should be similar
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
            s.add(int(str(n)[::-1]))
        return len(s)