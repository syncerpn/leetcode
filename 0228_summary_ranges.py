#1. two pointers, probably
def solve(nums: list) -> list:
    if not nums:
        return []
    s = nums[0]
    p = s
    result = []
    for n in nums[1:]:
        if n - p != 1:
            if s == p:
                result.append(f"{s}")
            else:
                result.append(f"{s}->{p}")
            s = n
        p = n
    
    if s == p:
        result.append(f"{s}")
    else:
        result.append(f"{s}->{p}")
    return result