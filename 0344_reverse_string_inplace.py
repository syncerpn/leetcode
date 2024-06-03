#1. simply swap
def sovle(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        c = s[i]
        s[i] = s[-1-i]
        s[-1-i] = c