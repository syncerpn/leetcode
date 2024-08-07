# not difficult
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            root, *files = path.split(" ")
            for f in files:
                name, content = f.split("(")
                content = content[:-1]
                if content not in d:
                    d[content] = []
                d[content].append(root + "/" + name)
        
        return [d[c] for c in d if len(d[c]) > 1]