# count it
class Solution:
    def digitCount(self, num: str) -> bool:
        f = [num.count(str(i)) == int(c) for i,c in enumerate(num)]
        return all(f)
