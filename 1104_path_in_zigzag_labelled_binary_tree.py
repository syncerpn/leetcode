# need to find the true labels, i.e. those we assign to node without zigzag rule
# traverse the tree with true label
# and only append result of zigzag label
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        i = 1
        while label >= (1 << i):
            i += 1
        
        if i % 2 == 0:
            label = (1<<i) - 1 - label + (1<<(i-1))
        label //= 2
        i -= 1

        while i > 0:
            if i % 2 == 0:
                ans.append((1<<i) - 1 - label + (1<<(i-1)))
            else:
                ans.append(label)
            label //= 2
            i -= 1
        return ans[::-1]