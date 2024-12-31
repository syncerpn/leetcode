# fairly good problem
# made me think for a while to optimize it
# but then still ended up with this
# failed to implement monostack with even more handling
# but this might be one of the way to make it better
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p = [0] + [pi for pi in itertools.accumulate(nums)]
        ans = -1
        for i, pi in enumerate(p):
            for j in range(max(0, i-r), i-l+1):
                if pi - p[j] > 0:
                    if ans == -1:
                        ans = pi - p[j]
                    ans = min(ans, pi - p[j])
        return ans