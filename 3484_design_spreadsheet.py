# dict
# surprisingly easier than the previous one
class Spreadsheet:

    def __init__(self, rows: int):
        self.d = {c: {} for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    def setCell(self, cell: str, value: int) -> None:
        c = cell[0]
        i = cell[1:]
        self.d[c][i] = value

    def resetCell(self, cell: str) -> None:
        c = cell[0]
        i = cell[1:]
        if i in self.d[c]:
            del self.d[c][i]

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        va, vb = 0, 0
        if a[0] in self.d:
            if a[1:] in self.d[a[0]]:
                va = self.d[a[0]][a[1:]]
        else:
            va = int(a)
        
        if b[0] in self.d:
            if b[1:] in self.d[b[0]]:
                vb = self.d[b[0]][b[1:]]
        else:
            vb = int(b)
        
        return va + vb


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)