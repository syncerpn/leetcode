# backtracking solution
class Solution:
    @functools.cache
    def punishmentNumber(self, n: int) -> int:
        if n == 1:
            return 1
        def partition(s, i, t, n):
            if i == len(s):
                return t == n
            for j in range(i, len(s)):
                v = t + int(s[i:j+1])
                if v > n:
                    return False
                if partition(s, j+1, v, n):
                    return True
            return False

        r = n * n if partition(str(n*n), 0, 0, n) else 0
        return r + self.punishmentNumber(n-1)

# this solution is faster
class Solution:
    @functools.cache
    def punishmentNumber(self, n: int) -> int:
        p_num = 0

        # Iterate through numbers in range [1, n]
        for curr_num in range(1, n + 1):
            sq_num = curr_num * curr_num

            # Check if valid partition can be found and add squared number if so
            if self.canPartition(sq_num, curr_num):
                p_num += sq_num

        return p_num
    
    # it is natural to add @cache here
    # but somehow it is much slower not to
    def canPartition(self, num, target):
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition
        return (
            self.canPartition(num // 10, target - num % 10)
            or self.canPartition(num // 100, target - num % 100)
            or self.canPartition(num // 1000, target - num % 1000)
        )