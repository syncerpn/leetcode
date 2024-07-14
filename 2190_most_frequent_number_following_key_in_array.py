# easy
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = {}
        most_freq = None
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in d:
                    d[nums[i+1]] = 0
                d[nums[i+1]] += 1
                if most_freq is None:
                    most_freq = nums[i+1]
                elif d[most_freq] < d[nums[i+1]]:
                    most_freq = nums[i+1]
        
        return most_freq