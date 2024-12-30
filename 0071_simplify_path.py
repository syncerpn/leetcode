# fairly simple with stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        ps = [p for p in path.split("/") if p]
        s = []
        for p in ps:
            if p == "..":
                if s:
                    s.pop()
            elif p == ".":
                continue
            else:
                s.append(p)
        return "/" + "/".join(s)