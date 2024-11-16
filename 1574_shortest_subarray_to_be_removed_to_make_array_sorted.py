# two pointer approach
# find the left sorted and right sorted subarray
# then find the shortest subarray in between
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1

        while l < n - 1:
            if arr[l] > arr[l+1]:
                break
            l += 1
        else:
            return 0
        
        while r > l:
            if arr[r-1] > arr[r]:
                break
            r -= 1
        
        ans = min(n - l - 1, r)
        i, j = 0, r
        while i <= l and j < n:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans