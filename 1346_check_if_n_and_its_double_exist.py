# just check with set
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for n in arr:
            if n << 1 in s or n / 2 in s:
                return True
            s.add(n)
        return False
        