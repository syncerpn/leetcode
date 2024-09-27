# may use tree or sorted linked list as well
# but i was lazy implementing those
# so just use list with binary search
# this should be O(logn) binary search + O(n) for insertion = O(n) overall
class MyCalendar:

    def __init__(self):
        self.s = []
        self.e = []

    def book(self, start: int, end: int) -> bool:
        if not self.s:
            self.s.append(start)
            self.e.append(end)
        else:
            i = bisect.bisect_left(self.s, start)
            if i == len(self.s):
                if self.e[i-1] > start:
                    return False
            else:
                if self.s[i] == start or end > self.s[i]:
                    return False
                if i > 0 and self.e[i-1] > start:
                    return False
            self.s.insert(i, start)
            self.e.insert(i, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)