# move the last to the last position and fix it
# then come the next one
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n-1
        ans = []
        while i >= 0:
            if arr[i] != i+1:
                j = 0
                while arr[j] != i+1:
                    j += 1
                ans.append(j+1)
                arr[:j+1] = arr[:j+1][::-1]
                ans.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]
            i -= 1
        return ans
