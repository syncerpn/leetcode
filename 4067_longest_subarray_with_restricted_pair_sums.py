# a bit long but works with general restriction
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        d = {}
        v = {}
        ans = 0
        for r in range(n):
            a = nums[r]
            while a in d:
                b = nums[l]
                v[b] -= 1
                if v[b] == 0:
                    del v[b]
                l += 1
                for i in range(l, r):
                    c = b + nums[i]
                    d[c] -= 1
                    if d[c] == 0:
                        del d[c]
            
            while True:
                dt = {}
                for i in range(l, r):
                    c = a + nums[i]
                    if c in v:
                        break
                    if c not in dt:
                        dt[c] = 0
                    dt[c] += 1
                else:
                    ans = max(ans, r - l + 1)
                    for k in dt:
                        if k not in d:
                            d[k] = 0
                        d[k] += dt[k]
                    break

                b = nums[l]
                v[b] -= 1
                if v[b] == 0:
                    del v[b]
                l += 1
                for i in range(l, r):
                    c = b + nums[i]
                    d[c] -= 1
                    if d[c] == 0:
                        del d[c]
            
            if a not in v:
                v[a] = 0
            v[a] += 1

        return ans

# for restricted element value 1 <= a <= 500
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums) * 2 + 1
        l = 0
        d = [0] * m
        v = [0] * m
        ans = 0
        for r in range(n):
            a = nums[r]
            while d[a]:
                b = nums[l]
                v[b] -= 1
                l += 1
                for i in range(l, r):
                    c = b + nums[i]
                    d[c] -= 1
            
            while True:
                dt = {}
                for i in range(l, r):
                    c = a + nums[i]
                    if v[c]:
                        break
                    if c not in dt:
                        dt[c] = 0
                    dt[c] += 1
                else:
                    ans = max(ans, r - l + 1)
                    for k in dt:
                        d[k] += dt[k]
                    break

                b = nums[l]
                v[b] -= 1
                l += 1
                for i in range(l, r):
                    c = b + nums[i]
                    d[c] -= 1
            v[a] += 1

        return ans