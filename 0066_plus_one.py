# set carry = 1 for ease of implementation; simply add carry
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                c = 0
                break
        if c:
            return [1] + digits
        return digits