# oneliner
# with xor to flip the bits
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[i^1 for i in row[::-1]] for row in image]