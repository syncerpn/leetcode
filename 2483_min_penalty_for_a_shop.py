# good init for the problem
# formulate the penalty with prefix sum
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        s = customers.count("Y")
        n = len(customers)
        ans, ans_i = s, 0
        t = 0
        for i in range(n):
            if customers[i] == "Y":
                t += 1
            p = i + 1 - t + s - t
            if p < ans:
                ans = p
                ans_i = i + 1
        return ans_i

# simplified a bit
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans, ans_i = 0, 0
        t = 0
        for i in range(n):
            if customers[i] == "Y":
                t += 1
            p = i + 1 - t - t
            if p < ans:
                ans = p
                ans_i = i + 1
        return ans_i

# transform a bit into reward instead of penalty
# now we maximize the reward, which is number of Y minus number of N so far
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans, ans_i = 0, -1
        t = 0
        for i in range(n):
            if customers[i] == "Y":
                t += 1
            else:
                t -= 1
            if t > ans:
                ans, ans_i = t, i
        return ans_i + 1