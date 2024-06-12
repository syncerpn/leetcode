#1. using XOR
#2. XOR a pair of the same number results in 0
#3. so if we XOR everything, the result will be equals to the single number
def solve(nums: list) -> int:
    x = 0
    for n in nums:
        x = x ^ n
    
    return x