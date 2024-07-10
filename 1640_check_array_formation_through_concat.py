# track the first element of each piece with hash table
# iterate the array
# now we can lookup the hash table can compare the piece with next k elements in the array
# all elements are distinct making it easy to use hash table
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        for p in pieces:
            d[p[0]] = p
        
        i = 0
        while i < len(arr):
            a = arr[i]
            if a not in d:
                return False
            i += 1
            j = 1
            while j < len(d[a]):
                if d[a][j] != arr[i]:
                    return False
                i += 1
                j += 1
        
        return True