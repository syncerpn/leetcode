# fairly easy with prefix sum or accumulate
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        acc = list(accumulate(differences, initial=0))
        return max(0, upper - lower - max(acc) + min(acc) + 1)