# parse and detach int from string
# then add them to a set for counting
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        DIGITS = "0123456789"
        j = 0
        nums = set()
        for i, c in enumerate(word + "#"):
            if c not in digits:
                if j != i:
                    nums.add(int(word[j:i]))
                j = i + 1

        return len(nums)