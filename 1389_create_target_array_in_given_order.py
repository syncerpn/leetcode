# insertion is trivial
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target

# there is an O(nlogn) solution, but it does not seem so appealing to me