# need revisit
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        drops = list(compress(count(), map(gt, nums, nums[1:])))  # j with nums[j] > nums[j + 1]

        def sortable(k):  # each drop needs its own block, which must wrap into order and fit between its neighbors
            if len(drops) > n // k:  # a block holds at most one drop
                return False
            prev_block = prev_drop = -1
            for j in drops:
                block, offset = divmod(j, k)
                start, end = j - offset, j - offset + k - 1
                if (offset == k - 1  # the drop sits on a border
                        or block == prev_block  # a second drop in the same block
                        or nums[end] > nums[start]  # the block can't wrap into order
                        or start and (nums[prev_drop] if prev_block == block - 1 else nums[start - 1]) > nums[j + 1]  # left block's max > this block's min
                        or end + 1 < n and nums[j] > nums[end + 1]):  # this block's max > the next value
                    return False
                prev_block, prev_drop = block, j
            return True

        small = [k for k in range(1, isqrt(n) + 1) if n % k == 0]
        divisors = {*small, *(n // k for k in small)}
        return sum(filter(sortable, divisors))
