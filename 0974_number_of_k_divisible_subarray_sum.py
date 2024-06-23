# using prefix sum, counting all number of mod_k occurence
# each pair of occurences should form one target subarray, thus n occurences form (n-1) * n // 2
# on the fly counting: each time a mod_k is increased, add its count to the answer
# if mod_k is zero, one extra is added because each single occurence counts
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        mod_k = 0
        d = {}
        for i, n in enumerate(nums):
            mod_k = (mod_k + n) % k
            if mod_k not in d:
                d[mod_k] = 0
            d[mod_k] += 1
            count += d[mod_k] - 1 + (mod_k == 0)
        
        return count