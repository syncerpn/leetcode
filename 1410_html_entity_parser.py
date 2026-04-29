# easy
class Solution:
    def entityParser(self, text: str) -> str:
        d = {
            "&quot;": "\"",
            "&apos;": "\'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }

        p = ""
        s = []
        for c in text:
            if c == "&":
                s.append(p)
                p = "&"
            elif c == ";":
                p += ";"
                if p in d:
                    s.append(d[p])
                else:
                    s.append(p)
                p = ""
            else:
                p += c
        s.append(p)
        return "".join(s)