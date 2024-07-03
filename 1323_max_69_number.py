# convert the first 6 into 9 (left to right)
# its best to do with string
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [c for c in str(num)]
        for i, c in enumerate(s):
            if c == "6":
                s[i] = "9"
                break
        return int("".join(s))