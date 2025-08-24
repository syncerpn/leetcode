# easy
# might be misleading if skimming the title too fast lol
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        d = Counter(nums)
        for a in d:
            if d[a] > n // k:
                return False
        return True