# divide the array into 4 parts
# then the target must be in one of the ends of the 4 parts
# confirm all the candidates with binary search
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        target = n / 4
        
        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate
            
        return -1

# or a more trivial way is to check if a number equals another number that is 25% length away from it
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        i = 0
        d = len(arr) // 4
        while arr[i] != arr[i+d]:
            i += 1
        return arr[i]