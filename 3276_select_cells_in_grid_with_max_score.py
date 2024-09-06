# this one is named hungarian problem
# check the cp algorithm to learn more about it
# note: this one was invalidated by the new test cases added after the contest
# they also invalidated my result as well lol
# #
# since the constraints are fairly small
# backtracking is obvious
# however, it was lte
# so some early stopping conditions are essential
# one of them is to calculate the max sum for all subsequent grid with prefix sum and sorting
# the following solution is made during the contest
# so it might not be very clean and compact
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        grid = [sorted(list(set(g)), reverse=True) for g in grid]
        acc = []
        t = 0
        for g in grid[::-1]:
            t += g[0]
            acc.append(t)
        acc = acc[::-1]
        m = len(grid)
        ans = [0]
        def backtrack(v, i, s):
            if i == m:
                ans[0] = max(ans[0], s)
            else:
                if s + acc[i] < ans[0]:
                    return True
                early_stop = False
                for c in grid[i]:
                    if c not in v:
                        v.add(c)
                        s += c
                        early_stop = backtrack(v, i+1, s)
                        s -= c
                        v.discard(c)
                    if early_stop:
                        break
                else:
                    backtrack(v, i+1, s)
            return False
        backtrack(set(), 0, 0)
        return ans[0]

# so i added this solution as reference
# this is from other guys
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # generate a sorted list of (value, row, col) in the grid.
        # this sorting will happen in lexographical order, just like
        # ordering something alphabetically. So, `value` will be the
        # most significant element, but if `value[i] == value[j], i != j`,
        # then the next most significant element is what row they
        # are in. 
        values = sorted([(grid[i][j], i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

        dp = {}
        def solve(i, rows):
            # If we've tried all of the values, just exit.
            # no more points to be gained.
            if i >= len(values):
                return 0

            # if we've already solved the path at this point,
            # from this index with this combination of rows already
            # selected, then simply return that cached result
            if (i, rows) in dp:
                return dp[(i, rows)]

            # will store the result
            res = 0
            # Each value in values is a tuple of (value, row, col). So,
            # here we get the row from the value at the current index
            # for this recusion step.
            cur_row = values[i][1]

            # here, we check if we have already selected a value
            # from the current row. If so, we'll just move on to the
            # next value in the list, skipping over this one, since
            # this one can't be selected.
            if (rows & (1 << cur_row)):
                res = solve(i+1, rows)
            # If we haven't already selected a value from this row,
            # then we have the option to either select one or not select one.
            # so there are two potential paths in the else block.
            else:
                # get the index of the next unique value.
                j = i
                while (j < len(values)) and (values[i][0] == values[j][0]):
                    j += 1
                
                # here, we select this value and continue at the index
                # of the next unique value (since values is sorted, and
                # we can't select two of the same value, this will be
                # the next smallest value). We use the OR operator to
                # set the bit corresponding with the row of this element
                # we're selecting in the `rows` bitmask.
                path1 = values[i][0] + solve(j, rows | (1 << cur_row))

                # Otherwise, we can choose not to select this value and
                # just move on to the next value in the values list.
                path2 = solve(i+1, rows)

                # the result will be the maximum of the two paths,
                # since we want to maximize our score:
                res = max(path1, path2)
            
            # cache and return the result
            dp[(i, rows)] = res
            return res

        # thanks to https://leetcode.com/u/virujthakur01/ for inspiring
        # this solution. I adapted the python code here from his C++ solution,
        # and used his solution to understand the problem and gain
        # the necessary insight and intuition to solve it.
        return solve(0,0)