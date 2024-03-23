# -*- coding: utf-8 -*-
#1. iterate through the list, add the number to a dict/set
#2. check whether its counterpart is already in the dict/set
def solve(nums: list, target: int) -> tuple:
    nums_dict = {}
    for n in nums:
        if target - n in nums_dict:
            return (n, target-n)
        nums_dict[n] = 1
    
    return ()