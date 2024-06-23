class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted = sorted(seats)
        studs_sorted = sorted(students)

        m = 0
        for a, b in zip(seats_sorted, studs_sorted):
            m += abs(a - b)
        return m