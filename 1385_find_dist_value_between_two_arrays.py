# use binary search on sorted arr2 for each n in arr1
# pretty nice solution
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        a = 0
        for n in arr1:
            l = 0
            r = len(arr2) - 1
            while l <= r:
                m = (l + r) // 2
                if abs(n - arr2[m]) <= d:
                    break
                elif n - arr2[m] > d:
                    l = m + 1
                else:
                    r = m - 1
            else:
                a += 1
        return a

# the following two pointer solution is also nice
# copied from others for reference
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist