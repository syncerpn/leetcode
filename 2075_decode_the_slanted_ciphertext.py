# easy
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        ans = []
        for j in range(cols):
            for i in range(min(cols - j, rows)):
                ans.append(encodedText[i * cols + j + i])
        
        return "".join(ans).rstrip()

# for some reasons this impl is much faster
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        N = len(encodedText)
        cols = N // rows
        i, j, k = 0, 0, 0
        original_text = []

        while k < N:
            original_text.append(encodedText[k])
            i += 1
            if i == rows:
                i = 0
                j += 1
            k = i*(cols + 1) + j

        return ''.join(original_text).rstrip()