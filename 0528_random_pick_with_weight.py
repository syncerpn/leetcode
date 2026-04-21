# pick is O(nlogn)
class Solution:

    def __init__(self, w: List[int]):
        self.W = []
        self.s = 0
        for wi in w:
            self.W.append(self.s)
            self.s += wi

    def pickIndex(self) -> int:
        r = random.randint(0, self.s - 1)
        i = bisect.bisect(self.W, r)
        return i-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# O(1) pick when you create n parts, each of which may have at most two indices
# just brilliant
class Solution:

    def __init__(self, w: List[int]):
        '''
        Create n uniform boxes of size 1/n each
        Fill them with (at most) 2 indices, and the weight associated with the first index
        O(n) time & space
        '''
        self.n = len(w)
        self.boxes = []
        
        ep = 10e-5
        summ = sum(w)
        weights = [elem / summ for elem in w]
        size = 1 / self.n
        big_weights = {i: x for i, x in enumerate(weights) if x >= size}
        small_weights = {i: x for i, x in enumerate(weights) if x < size}
        
        while big_weights and small_weights:
            # Pick a small and a big weight to make a full box
            i = next(iter(big_weights))
            j, w_j = small_weights.popitem()
            self.boxes.append([j, i, w_j])

            # The leftover from the big weight may now qualify as a small one
            big_weights[i] -= (size - w_j)
            if big_weights[i] < size - ep:  # I can't explain why it bugs if I remove that epsilon...
                small_weights[i] = big_weights.pop(i)
        
        self.boxes.extend([key] for key in big_weights)

    def pickIndex(self) -> int:
        '''
        Pick a random box (it has either 1 or 2 indices)
        If it has 2, randomly pick according to the relative weight between the two
        O(1) time & space
        '''
        box_num = random.randint(0, self.n - 1)
        
        if len(self.boxes[box_num]) == 1:
            return self.boxes[box_num][0]
        
        return self.boxes[box_num][random.uniform(0, 1 / self.n) >= self.boxes[box_num][2]]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()