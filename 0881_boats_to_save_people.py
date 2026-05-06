# easy
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n - 1
        ans = 0
        while l <= r:
            a = people[l]
            while r > l and people[r] + a > limit:
                ans += 1
                r -= 1
            if r > l:
                r -= 1
            ans += 1
            l += 1
        return ans