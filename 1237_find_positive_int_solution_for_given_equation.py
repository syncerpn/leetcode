# binary search is trivial
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        CONSTRAINTS_MIN = 1
        CONSTRAINTS_MAX = 1000
        x = CONSTRAINTS_MIN
        ans = []
        while customfunction.f(x, CONSTRAINTS_MIN) <= z:
            l = CONSTRAINTS_MIN
            r = CONSTRAINTS_MAX
            while l <= r:
                y = (l + r) // 2
                if customfunction.f(x, y) == z:
                    ans.append([x, y])
                    break
                elif customfunction.f(x, y) < z:
                    l = y + 1
                else:
                    r = y - 1
            
            x += 1
        return ans

# but binary search is actually not necessary
# we can use two pointer with linear time complexity
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        CONSTRAINTS_MIN = 1
        CONSTRAINTS_MAX = 1000
        x = CONSTRAINTS_MIN
        y = CONSTRAINTS_MAX

        ans = []

        while CONSTRAINTS_MAX >= x >= CONSTRAINTS_MIN and CONSTRAINTS_MAX >= y >= CONSTRAINTS_MIN:
            if customfunction.f(x, y) == z:
                ans.append([x, y])
                x += 1
                y -= 1
            elif customfunction.f(x, y) < z:
                x += 1
            elif customfunction.f(x, y) > z:
                y -= 1
        return ans