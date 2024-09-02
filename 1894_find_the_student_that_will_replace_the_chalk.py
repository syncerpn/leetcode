# fairly easy with prefix sum and binary search
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        t = 0
        for i in range(len(chalk)):
            t += chalk[i]
            chalk[i] = t
        return bisect.bisect_right(chalk, k % chalk[-1])