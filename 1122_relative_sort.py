# use hash table to save indices for quick lookup
# if not present in hash table, sorting score equals its value + length of arr2
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(arr2):
            d[n] = i
        return sorted(arr1, key=lambda x: d[x] if x in d else x + len(arr2))