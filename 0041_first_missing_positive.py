#1. try using two pointers
#2. inplace swap position such that a number should be place at its value-1 (nums[i] == i+1)
#3. junk numbers (too big or negative ones) put to the end
#4. iterate one more time for checking any out-of-place numbers; return that one
#5. if there is none out-of-place, return the next integer to be in the sequence
def solve(nums: list) -> int:
    i = 0
    j = len(nums) - 1
    while i <= j:
        n = nums[i]
        if n != i+1:
            if n > j+1 or n <= 0:
                nums[i] = nums[j]
                nums[j] = n
                j -= 1
            else:
                if nums[i] != nums[n-1]:
                    nums[i] = nums[n-1]
                    nums[n-1] = n
                else:
                    i += 1
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return i+2