#1. use dict to save indices for quick lookup
#2. if not present in dict, sorting score equals its value + length of arr2
def solve(arr1: list, arr2: list) -> list:
    d = {}
    for i, n in enumerate(arr2):
        d[n] = i
    return sorted(arr1, key=lambda x: d[x] if x in d else x + len(arr2))