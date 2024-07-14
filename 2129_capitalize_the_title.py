# just convert
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        for i, word in enumerate(words):
            words[i] = word.lower()
            if len(word) > 2:
                words[i] = words[i][0].upper() + words[i][1:]
        
        return " ".join(words)