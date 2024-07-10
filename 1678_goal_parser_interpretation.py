# make it cases
class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        n = len(command)
        r = ""
        while i < n:
            if i <= n-4 and command[i:i+4] == "(al)":
                r += "al"
                i += 4
            elif i <= n-2 and command[i:i+2] == "()":
                r += "o"
                i += 2
            else:
                r += command[i]
                i += 1
        return r
