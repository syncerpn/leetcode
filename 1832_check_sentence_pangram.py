# use a set to track chars appeared
# sentence is pangram if set of chars has 26
# assume only lower case english chars by default
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = set()
        for c in sentence:
            if c not in a:
                a.add(c)
        
        return len(a) == 26