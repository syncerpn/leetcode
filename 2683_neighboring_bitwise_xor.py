# easy
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for a in derived:
            ans ^= a
        return ans == 0

# learn using reduce
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda x, y: x ^ y, derived) == 0