# brute force simulation is trivial but not good
# this solution is math-based
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # find the number of distribution turns
        # i.e. find the closest k such that k * (k + 1) // 2 < candies
        # the formula for find k as below is just beautiful
        k = int((math.sqrt(1 + 8 * candies) - 1) / 2)

        # encode k into number of cycles p (passed through every people)
        # and the remaining q
        p = k // num_people
        q = k  % num_people

        # r is the remaining candies for the last turn
        r = candies - k * (k + 1) // 2

        # number of distributed candies can be calculated like below
        a = [(i + 1) * p + p * (p - 1) // 2 * num_people for i in range(num_people)]

        for i in range(q + 1):
            if i < q:
                a[i] += num_people * p + i + 1
            elif i == q:
                a[i] += r

        return a