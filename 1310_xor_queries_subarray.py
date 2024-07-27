# prefix xor
# was overthinking using segmented tree with this one
# but then found that unxor is pretty easy
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x = 0
        for i, a in enumerate(arr):
            x ^= a
            arr[i] = x
        
        arr = [0] + arr
        ans = []
        for l, r in queries:
            ans.append(arr[r+1] ^ arr[l])
        
        return ans