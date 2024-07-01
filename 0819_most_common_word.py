# split into words then check
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split("\!|\?|\'|\,|\;|\.| ", paragraph.lower())
        banned = set(banned)
        d = {}
        c_max = 0
        most_common = ""

        for word in words:
            if word in banned or word == "":
                continue
            if word not in d:
                d[word] = 0
            d[word] += 1
            if c_max < d[word]:
                c_max = d[word]
                most_common = word
        
        return most_common