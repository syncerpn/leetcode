# binary search
# and you can compare char directly instead of using their ascii value
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        a = 0
        while l <= r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m - 1
                a = m
            else:
                l = m + 1
        
        return letters[a]