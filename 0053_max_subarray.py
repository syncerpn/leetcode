#1. kadane's algorithm again; just beautiful
def solve(nums: list) -> int:
    d = nums[0]
    max_d = d
    for n in nums[1:]:
        d = max(d + n, n)
        if max_d < d:
            max_d = d
    return max_d