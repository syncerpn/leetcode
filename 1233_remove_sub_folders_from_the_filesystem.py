# my trie solution
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))
        root = {"/": {}}
        def add(f):
            n = root
            is_new = False
            for c in f:
                if c in n:
                    n = n[c]
                else:
                    if not is_new and c == "/":
                        return False
                    is_new = True
                    n[c] = {}
                    n = n[c]
            return True
        
        ans = []
        for f in folder:
            if add(f):
                ans.append(f)
        return ans

# actually, we can just sort it and go through the list
# by sorting, we can guarantee meeting subfolders after a folder if any
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        ans = []
        p = ""
        for f in folder:
            if not p or not f.startswith(p + '/'):
                ans.append(f)
                p = f
        return ans