# i was overthinking this one, lol
# we just need to make sure the last digit is not 0
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0