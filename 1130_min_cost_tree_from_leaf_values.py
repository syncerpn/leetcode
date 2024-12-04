# try all the ways to divide the arr and form the tree
# with memoi to save time
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cache = {}
        def helper(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            if l >= r:
                return 0
        
            ans = (1 << 32) - 1
            for m in range(l, r):
                ans = min(ans, max(arr[l:m+1]) * max(arr[m+1:r+1]) + helper(l, m) + helper(m+1, r))
            cache[(l, r)] = ans
            return ans
        return helper(0, len(arr)-1)

# this is even faster
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # greedy approach
        res = 0

        while len(arr) > 1:
            min_idx = arr.index(min(arr))

            if min_idx == 0:
                res += arr[min_idx] * arr[min_idx+1]
            elif min_idx == len(arr)-1:
                res += arr[min_idx] * arr[min_idx-1]
            else:
                res += arr[min_idx] * min(arr[min_idx+1], arr[min_idx-1])

            # delete the min number because it will never be used again
            arr.pop(min_idx)

        return res

# lee always makes it optimal, monostack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res