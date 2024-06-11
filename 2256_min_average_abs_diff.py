def solve(nums: list) -> int:
    acc = 0
    for n in nums:
        acc += n
    
    l = len(nums)
    right = 0
    d = acc // l
    k = l - 1
    
    i = l - 2
    while i >= 0:
        n = nums[i+1]
        right += n
        acc -= n
        di = abs(right // (l-1-i) - acc // (i+1))
        if d >= di:
            d = di
            k = i
        i -= 1
    
    return k