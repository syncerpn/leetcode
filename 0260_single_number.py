#1. calculate xor of all numbers; in the end, this equals xor of the two single numbers
#2. (with math proof) find a separator d equals and of the above result with its opposite
#3. the separator can divide the list into 2, and xor of two lists results in the two single numbers
def solve(nums: list) -> list:
    x = 0
    for n in nums:
        x ^= n
    
    d = x & -x

    a = 0
    b = 0
    for n in nums:
        if n & d == 0:
            a ^= n
        else:
            b ^= n
    
    return [a, b]