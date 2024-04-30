#1. iterate through the list, add the number to a dict
#2. check whether its counterpart is already in the dict
def solve(nums: list, target: int) -> list:
    nums_dict = {}
    for i, n in enumerate(nums):
        if target - n in nums_dict:
            return [i, nums_dict[target-n]]
        nums_dict[n] = i
    
    return []