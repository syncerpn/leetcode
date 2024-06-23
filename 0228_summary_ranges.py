# two pointers, probably
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = nums[0]
        p = s
        result = []
        for n in nums[1:]:
            if n - p != 1:
                if s == p:
                    result.append(f"{s}")
                else:
                    result.append(f"{s}->{p}")
                s = n
            p = n
        
        if s == p:
            result.append(f"{s}")
        else:
            result.append(f"{s}->{p}")
        return result