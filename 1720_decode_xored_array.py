class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        arr = [first] * (n + 1)
        for i in range(n):
            arr[i+1] = arr[i] ^ encoded[i]
        return arr