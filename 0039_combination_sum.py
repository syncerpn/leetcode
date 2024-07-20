# pretty good problem to think of a backtracking algorithm
# i ended up implementing on myself to get used to it
# yet still not very confident
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        c, s = [0], candidates[0]

        result = []
        while c:
            if s < target:
                # append the same as previous one in the stack is the key
                c.append(c[-1])
                s += candidates[c[-1]]
            else:
                if s == target:
                    result.append([candidates[i] for i in c])
                s -= candidates[c[-1]]
                c.pop()
                while c and c[-1] == n - 1:
                    s -= candidates[n-1]
                    c.pop()
                if c:
                    s -= candidates[c[-1]]
                    c[-1] += 1
                    s += candidates[c[-1]]

        return result