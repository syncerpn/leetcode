#1. O(n) solution by tracking third, second, first max index accordingly
def solve(nums: list) -> int:
    f = -1
    s = -1
    t = -1
    for i, n, in enumerate(nums):
        if f == -1:
            f = i
        elif n > nums[f]:
            t, s, f = s, f, i
        elif n == nums[f]:
            continue
        elif s == -1:
            s = i
        elif n > nums[s]:
            t, s = s, i
        elif n == nums[s]:
            continue
        elif t == -1:
            t = i
        elif n != nums[s] and n > nums[t]:
            t = i
    
    if t == -1:
        return nums[f]
    return nums[t]