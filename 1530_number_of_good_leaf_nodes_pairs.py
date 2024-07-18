# this solution is just beautiful, as well as comply with tree solving style
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        # we will break it down into counting good pairs in each subtree left and right
        # then we will do cross subtree pairs
        def solve(root):
            if not root:
                return {}
            if not root.left and not root.right:
                return {1:1}
            
            # count good pairs in each subtree
            l_to_root = solve(root.left)
            r_to_root = solve(root.right)

            # count good pairs in cross subtree
            for ld in l_to_root:
                for rd in r_to_root:
                    if ld + rd <= distance:
                        self.result += l_to_root[ld] * r_to_root[rd]
            
            # we traversal each subtree, finding leaves
            # then track, only, the distance from each leaf to the root
            # at this step, we dont need to care about cross subtree yet
            # because, it will eventually be considered later
            # if closely look at the code, this is cross subtree distance tracking
            # of the current node's subtrees
            d = {}
            
            for ld in l_to_root:
                # we dont need to care about those with already higher than target distance
                # because cross subtree later will just increases the total distance
                if ld + 1 > distance:
                    continue
                if ld + 1 not in d:
                    d[ld + 1] = 0
                d[ld + 1] += l_to_root[ld]
                
            for rd in r_to_root:
                # do the same for the right subtree
                if rd + 1 > distance:
                    continue
                if rd + 1 not in d:
                    d[rd + 1] = 0
                d[rd + 1] += r_to_root[rd]
            
            return d
        
        solve(root)
        return self.result

# this is my brute-force version
# though not good, it passed the tests
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def leaves_search(root, ancestor):
            if not root.left and not root.right:
                return [ancestor]
            r = []
            if root.left:
                r += leaves_search(root.left, ancestor + "L")
            if root.right:
                r += leaves_search(root.right, ancestor + "R")
            return r
        
        def get_distance(a, b):
            i = 0
            while i < len(a) and i < len(b):
                if a[i] != b[i]:
                    break
                i += 1

            return len(a) + len(b) - 2 * i

        c = 0
        leaves = leaves_search(root, "")
        for i in range(len(leaves)-1):
            for j in range(i+1, len(leaves)):
                if get_distance(leaves[i], leaves[j]) <= distance:
                    c += 1
        return c