#1. loop subarray
#2. find all subarrays that xor of all elements equals to 0
#3. if that is the case, we can form l-1 such triplet
def solve(arr: list) -> int:
    count = 0
    for i in range(len(arr)):
        x = arr[i]
        for j in range(i+1, len(arr)):
            x = x ^ arr[j]
            if x == 0:
                count += j-i
    
    return count