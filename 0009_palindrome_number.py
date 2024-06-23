# string manip
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# true numerical reverse
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = 0
        z = x
        while z > 0:
            d = z % 10
            y = y * 10 + d
            z = z // 10
        
        return x == y

# reverse only half of the input should be enough
# need to eliminate some edge cases other than negative x
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        y = 0
        while x > y:
            d = x % 10
            y = y * 10 + d
            x = x // 10
        
        return x == y or x == y // 10