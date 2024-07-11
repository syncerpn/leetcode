# keep track of unique values with set
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = set()
        non_unique = set()
        for n in nums:
            if n not in unique and n not in non_unique:
                unique.add(n)
            elif n not in non_unique:
                unique.discard(n)
                non_unique.add(n)
        
        return sum(unique)