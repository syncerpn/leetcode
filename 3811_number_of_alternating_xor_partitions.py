# nice and pretty difficult problem
# need to think in a different way
# formulate a state-dp
# where at some points in the array, a partition may end up in a state
# state is xor of the whole array and can be:
# after 0 block:  0
# after 1 block:  target1
# after 2 blocks: target1 ^ target2
# after 3 blocks: target1 ^ target2 ^ target1 = target2
# after 4 blocks: target1 ^ target2 ^ target1 ^ target2 = 0
# so, we can see it have only 4 states
# if we arrive at a state i, counts the way to arrive at state (i-1) % 4
# except for the last one, we must make sure we can arrive at a valid state
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD = 10 ** 9 + 7
        states = [0, target1, target1 ^ target2, target2]
        dp = [1, 0, 0, 0]
        
        p = 0
        last = nums.pop()

        for a in nums:
            p ^= a
            dp_n = dp[:]
            for i in range(4):
                if p == states[i]:
                    dp_n[i] += dp[(i-1)%4]
            dp = dp_n
        
        p ^= last
        return sum(dp[(i-1)%4] for i in range(4) if p == states[i]) % MOD

# will be quite faster if we do MOD on intermediate values
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD = 10 ** 9 + 7
        states = [0, target1, target1 ^ target2, target2]
        dp = [1, 0, 0, 0]

        p = 0
        last = nums.pop()

        for a in nums:
            p ^= a
            dp_n = dp[:]
            for i in range(4):
                if p == states[i]:
                    dp_n[i] = (dp_n[i] + dp[(i-1)%4]) % MOD
            dp = dp_n
        
        p ^= last
        return sum(dp[(i-1)%4] for i in range(4) if p == states[i]) % MOD