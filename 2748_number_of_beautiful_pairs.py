# brute-force version
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        c = 0
        for i in range(len(nums)-1):
            a = int(str(nums[i])[0])
            for j in range(i+1, len(nums)):
                b = int(str(nums[j])[-1])
                if gcd(a, b) == 1:
                    c += 1
        return c

# partition hash update as usual
# this pattern is just beautiful after you got it
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        COPRIMES = {"11","12","13","14","15","16","17","18","19","23",
                    "25","27","29","34","35","37","38","45","47",
                    "49","56","57","58","59","67","78","79","89"}
        d = {}
        r = 0

        i = 1
        while i < len(nums):
            fj = str(nums[i-1])[0]
            d[fj] = 1 if fj not in d else d[fj] + 1

            li = str(nums[i])[-1]

            for fj in d:
                p = fj + li if fj < li else li + fj
                if p in COPRIMES:
                    r += d[fj]
            i += 1
        
        return r