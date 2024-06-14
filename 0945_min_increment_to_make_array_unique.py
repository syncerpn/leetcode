#1. sorting then check for unique O(nlogn)
def solve(nums: list) -> int:
    nums = sorted(nums)
    m = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            p = nums[i-1] + 1 - nums[i]
            m += p
            nums[i] += p
    return m

#2. or union-find O(n)??
def solve2(nums: list) -> int:
    root = {}
    def find(x):
        root[x] = find(root[x] + 1) if x in root else x
        return root[x]
    return sum(find(a) - a for a in nums)