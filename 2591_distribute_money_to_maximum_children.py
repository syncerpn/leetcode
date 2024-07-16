# it needs math
# and was beautifully solved
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > children * 8:
            return children - 1
        k = (money - children) // 7
        r = money - 8 * k
        if r == 4 and children - k == 1:
            k -= 1
        return k