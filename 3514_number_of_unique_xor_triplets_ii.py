# brute-force is still acceptable considering the max value of each number
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                pairs.add(nums[i] ^ nums[j])
        
        triplets = set()
        for p in pairs:
            for a in nums:
                triplets.add(p ^ a)
        
        return len(triplets)