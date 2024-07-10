# dont need to simulate the process
# we just need to count number of 1 and 0 in students
# then try to feed student according to sandwiches stack
# while keeping track of students' need (1 or 0)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        m = sum(students)
        i = 0
        while i < len(sandwiches):
            k = sandwiches[i]
            if k == 1:
                if m == 0:
                    break
                m -= 1
            else:
                if m == n:
                    break
            n -= 1
            i += 1
        
        return len(sandwiches) - i