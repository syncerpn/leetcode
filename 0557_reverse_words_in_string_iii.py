#1. became one-liner for this one, lol
def solve(s: str) -> str:
    return " ".join([si[::-1] for si in s.split(" ")])