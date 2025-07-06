# hashmap makes it easy
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.d1 = Counter(nums1)
        self.d2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        a = self.nums2[index]
        self.d2[a] -= 1
        if self.d2[a] == 0:
            del self.d2[a]
        a += val
        self.nums2[index] = a
        self.d2[a] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for a in self.d1:
            if tot - a in self.d2:
                ans += self.d2[tot-a] * self.d1[a]
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)