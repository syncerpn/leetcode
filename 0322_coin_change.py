# learn a lot from this
# leave a quote from the discussion describes it all
# Take coins=[1,2,5] and amount = 11 as an example,
# If I use one 1, I need to know the fewest number of coins I need to make up 10, i.e., dp[10]. Overall I need 1+dp[10] coins.
# If I use one 2, I need 1+dp[9] coins.
# If I use one 5, I need 1+dp[6] coins.
# Therefore, I need to calculate dp from 1 to amount.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i and dp[i-c] != -1:
                    dp[i] = dp[i-c] + 1 if dp[i] == -1 else min(dp[i], dp[i-c] + 1)
        return dp[amount]
