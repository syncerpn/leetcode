# very nice "easy" problem touching monostack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        n = len(prices)
        r = [p for p in prices]
        # we will iterate backward the prices array
        # trying to build mono increasing stack
        for i in range(n-1, -1, -1):
            pi = prices[i]
            # because we travel backward
            # always make sure we keep the top of stack is smaller than currently checking prices[i]
            while s and s[-1] > pi:
                s.pop()
            
            # if there is something in the stack
            # top of the stack must be the next smaller element comparing to prices[i]
            # therefore, it is the discount of prices[i]
            if s:
                r[i] = pi - s[-1]
            # either stack is empty, or the top of stack is guaranteed to be smaller than prices[i]
            # push the current prices[i] into stack without worrying about mono increasing characteristic
            s.append(pi)
        return r

# the following solution is also nicely done with stack and forward traversal
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        # we iterate forward
        # pi will be used to check if it is valid as a discount value at indices of prices stored in s
        for i, pi in enumerate(prices):
            while s and prices[s[-1]] >= pi:
                # if pi is a valid discount value
                # we subtract it to the prices value with index at the top of the stack
                j = s.pop()
                prices[j] -= pi

            # again, pi is used to check as a valid discount
            # we store the index in s to update its value later
            # with pj (j > i) in the next iterations as discount of pi
            s.append(i)
        return prices