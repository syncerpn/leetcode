# have seen several submissions
# yet mine is truely inplace
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        c = 0
        n = len(arr)
        i = 0
        # we are going to find index i
        # up to which the numbers will stay in arr after zero insertion
        while i + c < n:
            if arr[i] == 0:
                c += 1
            i += 1
        
        # starting from this point, going backward
        # rearrange num at index i to index j of arr
        # assign zero to index j-1 if arr at index i is zero
        j = i + c - 1
        i -= 1
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                arr[j-1] = 0
                j -= 1
            j -= 1
            i -= 1