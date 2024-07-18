# check #0421
# anything with trie is really difficult
# the point of this is to apply the sliding window in #2932
# but we need trie to find the max xor faster than just xor everything in brute force manner
# trie will be used to hold bit information
# to maximize xor result
# going from most significant bit, trying to find different bit than the currently considering number
# for example, if nums[j] has 1 at position 13, then its max-xor counterpart better has 0 at 13
# but if we dont have one satisfying yet, go for another number
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # the trie need to how freq of bit as well
        # the point is that we want to remove number from trie as well
        trie_root = {}
        B = 19

        def add(n):
            node = trie_root
            b = B
            while b >= 0:
                p = (n >> b) & 1
                if p not in node:
                    node[p] = [{}, 0]
                node[p][1] += 1
                node = node[p][0]
                b -= 1

        def find_xor_max_counterpart(n):
            node = trie_root
            b = B
            m = 0
            while b >= 0:
                p = (n >> b) & 1
                if 1-p in node and node[1-p][1] > 0:
                    p = 1-p
                m |= p << b
                node = node[p][0]
                b -= 1
            return m

        def remove(n):
            node = trie_root
            b = B
            while b >= 0:
                p = (n >> b) & 1
                node[p][1] -= 1
                node = node[p][0]
                b -= 1

        # the same sliding window brute-force
        # but we add and remove nums from trie as going
        nums.sort()
        x = 0
        i = 0
        for j in range(1, len(nums)):
            add(nums[j-1])
            while nums[i] + nums[i] < nums[j]:
                remove(nums[i])
                i += 1
            if i == j:
                continue
            m = find_xor_max_counterpart(nums[j])
            x = max(x, m ^ nums[j])
        
        return x

# binary prefix solution
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = 0
        for i in range(20, -1, -1):
            res <<= 1
            pref, pref2 = {}, {}
            for a in nums:
                p = a >> i
                if p not in pref:
                    pref[p] = pref2[p] = a
                pref[p] = min(pref[p], a)
                pref2[p] = max(pref2[p], a)
            for x in pref:
                y = res ^ 1 ^ x
                if x >= y and y in pref and pref[x] <= pref2[y] * 2:
                    res |= 1
                    break
        return res