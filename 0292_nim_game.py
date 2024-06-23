# as long as your move results in a number of stones divisible by 4, you will win
# and the only case you cant make it is when the number of stones divisible by 4 at the beginning
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0