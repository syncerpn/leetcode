# first hand on segment tree, which might seem very useful as an advanced data structure
# the point of segment tree is to make every operation such as modify and query becomes O(logn)
class NumArray:

    def __init__(self, nums: List[int]):
        self.l = None
        self.r = None
        self.s = 0
        self.n = len(nums)
        if self.n == 1:
            self.s = nums[0]
        elif self.n > 1:
            self.l = NumArray(nums[:self.n//2])
            self.r = NumArray(nums[self.n//2:])
            self.s = self.l.s + self.r.s

    def update(self, index: int, val: int) -> None:
        if not self.l:
            assert index == 0
            self.s = val
        else:
            if index < self.n // 2:
                self.l.update(index, val)
            else:
                self.r.update(index - self.n // 2, val)
            self.s = self.l.s + self.r.s

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            left, right = right, left
        if left <= 0 and right >= self.n-1:
            return self.s
        if left >= self.n or right < 0:
            return 0
        return self.l.sumRange(left, right) + self.r.sumRange(left - self.n // 2, right - self.n // 2)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)