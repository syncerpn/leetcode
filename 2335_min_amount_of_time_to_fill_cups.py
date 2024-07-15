# very good problem
# my strategy at first was to either
# 1. if sum of two smaller cups is smaller than the biggest one,
# all we can do is to keep filling the biggest one + either of the rest each time
# then we still need to fill the biggest one more
# in total, it takes the same number of turns as the amount of water in the biggest cup
# 2. the other case, we keep filling the two smaller ones until condition 1 reaches
# and we can calculate exactly the number of steps to do so before condition 1 reaches
# it is the different amount divides by 2 and take round up
# here i used a small trick with int division
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        a, b, c = amount
        if a + b <= c:
            return c
        return abs((c - a - b) // 2) + c

# so, someone even proved that we can do like this
# based on ultimate math
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)