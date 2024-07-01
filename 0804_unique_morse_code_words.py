# simply transform and add to set
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpb = "abcdefghijklmnopqrstuvwxyz"
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {a: c for a, c in zip(alpb, code)}
        s = set()
        for w in words:
            t = ""
            for c in w:
                t += d[c]
            s.add(t)
        
        return len(s)