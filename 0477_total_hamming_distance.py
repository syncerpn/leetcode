# math proof
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 1. Coordinate Manifold Transformation
        # Convert integers into a bit-matrix of shape (N, 32)
        # We use a bitwise right shift and mask to extract each bit vectorized
        import numpy as np
        X = np.array(nums, dtype=np.uint32).reshape(-1, 1)
        shifts = np.arange(32, dtype=np.uint32)
        
        # 2. Bitwise Projection
        # Extract the bit-manifold: bits[i, j] is the j-th bit of nums[i]
        bits = (X >> shifts) & 1
        
        # 3. Frequency Analysis
        # Count 1s in each column (bit position)
        c1 = np.sum(bits, axis=0)
        c0 = len(nums) - c1
        
        # 4. Combinatorial Sum
        # Each pair of (0, 1) at a position contributes 1 to the Hamming distance
        return int(np.sum(c1 * c0))     
        