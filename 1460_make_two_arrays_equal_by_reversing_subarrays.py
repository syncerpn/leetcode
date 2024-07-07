# simply count and make sure the number of each element matches
# this is O(n) time and space
# or you can sort them for O(nlogn) time and O(1) space
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        d = {}
        for n in target:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        for n in arr:
            if n not in d:
                return False
            d[n] -= 1
            if d[n] < 0:
                return False
        return True