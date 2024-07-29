# anchor j
# then search for left smaller i and right greater k
# O(n2) time
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for j in range(1, n-1):
            l, r = 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    l += 1
            for k in range(j+1, n):
                if rating[k] > rating[j]:
                    r += 1
            ans += l * r + (j - l) * (n-1-j-r)
        return ans

# there is a solution with sorting that can achieve O(nlogn) as well