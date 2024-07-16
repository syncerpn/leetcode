# find spaces with single pass O(n) time O(1) space
# dont even need splitting
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, c in enumerate(sentence):
            if c == " ":
                if sentence[i-1] != sentence[i+1]:
                    return False
        
        return sentence[0] == sentence[-1]