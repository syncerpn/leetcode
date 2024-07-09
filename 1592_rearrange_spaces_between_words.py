# pretty simple
class Solution:
    def reorderSpaces(self, text: str) -> str:
        text_list = text.split(" ")
        words = []
        spaces = 0
        for t in text_list:
            if t != "":
                words.append(t)
            else:
                spaces += 1
        
        d = len(words) - 1
        spaces += d
        if spaces == 0:
            return text
        if d == 0:
            return words[0] + " " * spaces
        return (" " * (spaces // d)).join(words) + " " * (spaces % d)