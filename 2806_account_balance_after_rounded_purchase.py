# thought it was easy
# it was actuall not
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - round(purchaseAmount / 10 + 0.01) * 10