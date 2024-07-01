class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
        d = {}
        for c in licensePlate.lower():
            if c not in ALPHABET:
                continue
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        ws = None
        for word in words:
            wl = word.lower()
            t = {}
            for c in wl:
                if c not in d:
                    continue
                if c not in t:
                    t[c] = 0
                t[c] += 1
            for c in d:
                if c not in t or t[c] < d[c]:
                    break
            else:
                if ws is None or len(ws) > len(wl):
                    ws = word
        
        return ws
