# nice problem touches sliding window and maybe queue
# this one is not optimized, but may be easy to understand
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0

        # here i use a queue to track the first element of the flipped subarray
        # some elements may be under multiple flipping
        # it can be check by their index is within first element and first element + k
        flip_queue = deque()

        for i, n in enumerate(nums):
            while flip_queue:
                if i < flip_queue[0] + k:
                    break
                # remove those which have done flipping
                flip_queue.popleft()
            
            # length of the queue determines how many flipping are in effect
            # modulo of the length tells the target value to be flipped
            if n == (len(flip_queue) % 2):
                # flipping starting from here wont work
                # return impossible
                if i + k > len(nums):
                    return -1
                flip_queue.append(i)
                res += 1

        return res

# the following solution encodes flipping mark in nums to reduce space complexity
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        j = 0

        for i, n in enumerate(nums):
            if i >= k:
                if nums[i-k] == 2:
                    j ^= 1 # toggle j as one flipping effect expired
            
            if n == j:
                if i + k > len(nums):
                    return -1

                res += 1
                j ^= 1 # toggle j as one flipping effect starts
                nums[i] = 2
        
        return res