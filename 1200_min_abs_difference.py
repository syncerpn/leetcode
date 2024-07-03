# sort and check
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d_min = arr[-1] - arr[0]
        r = []
        for i in range(len(arr)-1):
            if d_min > arr[i+1] - arr[i]:
                r = []
                d_min = arr[i+1] - arr[i]
            if d_min == arr[i+1] - arr[i]:
                r.append([arr[i], arr[i+1]])
        return r
