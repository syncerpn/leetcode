# simply iterate over all possible cases
# some suggest backtracking, but is it that necessary?
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        r = [""]
        for d in digits:
            r = [ri + c for c in m[d] for ri in r]
        return r