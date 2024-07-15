# quite good problem
# we need to remove the one that followed by a larger number
# if that does not exist, remove the last occurence of the digit
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        j = 0
        for i in range(len(number)):
            if number[i] == digit:
                j = i
                if i == len(number) - 1:
                    return number[:-1]
                else:
                    if number[i+1] > digit:
                        return number[:i] + number[i+1:]
        return number[:j] + number[j+1:]