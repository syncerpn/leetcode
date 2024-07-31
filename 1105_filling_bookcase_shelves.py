# could not solve it myself with dfs at first
# this is copied from others
# solution is based on dp
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        CONSTRAINTS_MAX = 1000000
        n = len(books)
        dp = [CONSTRAINTS_MAX] * (n + 1) # dp[i]: height for books 0 to i - 1
        dp[0] = 0 # no book, no height
        for i in range(1, n + 1):
            # assume we opened up a new row for book i - 1
            curr_width, curr_height = shelfWidth, 0
            j = i - 1
            # what if we move previous books one by one to current row, while there's space, will it produce smaller height overall?
            # stop when the row is full, or no more books left
            while j >= 0 and curr_width - books[j][0] >= 0:
                # put book j into current row & update info
                # curr_width: remaining space in current row after putting in book j                         
                # curr_height: height of the tallest book in current row
                curr_width -= books[j][0]
                curr_height = max(curr_height, books[j][1])
                # dp[j]: the min height after removing some books until there's j left (or, the last book on shelf is book j - 1)
                # dp[j] + curr_height: add current row's height with books j, j+1, ..., i-1
                dp[i] = min(dp[i], dp[j] + curr_height)
                j -= 1
        return dp[n]
        