# easy
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        c = 0
        for m in message:
            if m in bannedWords:
                c += 1
                if c >= 2:
                    return True
        return False