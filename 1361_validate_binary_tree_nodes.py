# find root and traverse the graph
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        R = [0] * n
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                R[l] += 1
            if r != -1:
                R[r] += 1
        
        root = -1
        for i, a in enumerate(R):
            if a == 0:
                if root != -1:
                    return False
                root = i
            elif a != 1:
                return False
        
        v = set([root])
        s = [root]
        while s:
            node = s.pop()
            l, r = leftChild[node], rightChild[node]
            if l != -1:
                if l in v:
                    return False
                s.append(l)
                v.add(l)
            if r != -1:
                if r in v:
                    return False
                s.append(r)
                v.add(r)
        return len(v) == n