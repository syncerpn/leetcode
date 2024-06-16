#1. use #0031 to find next permutation of n; then simply do condition checking before return
def solve(n: int) -> int:
    def next_permutation(nums: list) -> None:
        n = len(nums)
        if n > 1:
            t = nums[0]
            for i in range(n-1, 0, -1):
                a = nums[i-1]
                b = nums[i]
                if a < b:
                    t = a
                    break
            else:
                i = 0
            
            print(i)
            if i > 0:
                for j in range(n-1, i-1, -1):
                    if nums[j] > t:
                        a = nums[j]
                        nums[j] = nums[i-1]
                        nums[i-1] = a
                        break
            
            j = i
            k = n-1
            while k > j:
                a = nums[j]
                nums[j] = nums[k]
                nums[k] = a
                
                k -= 1
                j += 1

    digits = []
    m = n
    while m:
        digits = [m % 10] + digits
        m //= 10
    
    next_permutation(digits)
    p = 0
    for d in digits:
        p = p * 10 + d
    
    if p > n and p <= (1 << 31) - 1:
        return p
    return -1