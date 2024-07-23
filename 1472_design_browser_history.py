# why no one uses two pointers and a single stack
# it reduces space and memory allocation
# it is just beautiful
class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.j = 0
        self.p = [homepage]        

    def visit(self, url: str) -> None:
        self.i += 1
        if self.i >= len(self.p):
            self.p.append(url)
        else:
            self.p[self.i] = url
        self.j = self.i

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.p[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.j, self.i + steps)
        return self.p[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)