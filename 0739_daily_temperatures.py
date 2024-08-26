# O(1) space O(n) time
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]:
                if ans[j] > 0:
                    j += ans[j]
                else:
                    ans[i] = 0
                    break
            else:
                ans[i] = j - i
        return ans

# monostack solution
# we build a monodec stack
# until we found one that is higher than the top of stack
# this must be the day we need to find for that top value of stack
# pop and check until the monostack can be maintained
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        s = []
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                j = s.pop()
                ans[j] = i - j
            s.append(i)
        return ans