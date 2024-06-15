#1. i think it is fair to use two-way dict
def solve(num1: str, num2: str) -> str:
    NUMS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    CHRS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    c = 0
    if len(num1) < len(num2):
        num1 = "0" * (len(num2) - len(num1)) + num1
    else:
        num2 = "0" * (len(num1) - len(num2)) + num2
    
    res = ""
    for d1, d2 in zip(num1[::-1], num2[::-1]):
        s = NUMS[d1] + NUMS[d2] + c
        c = s > 9
        res = CHRS[s % 10] + res
    
    return "1" + res if c else res