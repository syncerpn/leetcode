# need revisit
# 2 sets
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        bot = SortedList()
        top = SortedList()
        d = Counter()
        s = [0]

        def update(a, ca):
            if d[a]:
                try:
                    bot.remove([d[a], a])
                except:
                    top.remove([d[a], a])
                    s[0] -= d[a] * a

            d[a] += ca
            if d[a]:
                bot.add([d[a], a])

        ans = []
        for i in range(len(nums)):
            update(nums[i], 1)
            if i >= k:
                update(nums[i - k], -1)

            # rebalance
            while bot and len(top) < x:
                ca, a = bot.pop()
                s[0] += ca * a
                top.add([ca, a])

            while bot and bot[-1] > top[0]:
                ca, a = bot.pop()
                cb, b = top.pop(0)
                s[0] += ca * a - cb * b
                bot.add([cb, b])
                top.add([ca, a])

            if i >= k - 1:
                ans.append(s[0])

        return ans