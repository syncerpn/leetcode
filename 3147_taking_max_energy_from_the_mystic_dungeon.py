# k subarrays kadane
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = energy[-1]
        n = len(energy)
        for i in range(k):
            j = i + k
            p = energy[i]
            while j < n:
                p = max(p + energy[j], energy[j])
                j += k
            ans = max(ans, p)
        return ans