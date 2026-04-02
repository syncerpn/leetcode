# greedy
# try to check all "T" in str1 and fill the answer with str2 at that position
# any filled position with a different character will result in invalidation
# fill the rest with a
# then check and change a to b if necessary
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)  # ? indicates a pending position
        
        # Process 'T'
        for i, b in enumerate(str1):
            if b != 'T':
                continue
            # The substring must match str2
            for j, c in enumerate(str2):
                v = ans[i + j]
                if v != '?' and v != c:
                    return ""
                ans[i + j] = c
        
        old_ans = ans
        ans = ['a' if c == '?' else c for c in ans]  # Initial default is 'a'
        
        # Process 'F'
        for i, b in enumerate(str1):
            if b != 'F':
                continue
            # Substring must not equal t
            if ''.join(ans[i: i + m]) != str2:
                continue
            # Locate the last pending position to modify
            for j in range(i + m - 1, i - 1, -1):
                if old_ans[j] == '?':  # Change 'a' to 'b'
                    ans[j] = 'b'
                    break
            else:
                return ""
        return ''.join(ans)

# z function
# optimize from O(mn) to O(m+n)
class Solution:
    def generateString(self, str1: str, str2: str) -> str:

        def calc_z(s: str) -> List[int]:
            n = len(s)
            z = [0] * n
            box_l, box_r = 0, 0  # z-box boundaries
            for i in range(1, n):
                if i <= box_r:
                    z[i] = min(z[i - box_l], box_r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    box_l, box_r = i, i + z[i]
                    z[i] += 1
            z[0] = n
            return z

        n, m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)
        
        # Process 'T' with Z-function
        z = calc_z(str2)
        pre = -m
        for i, b in enumerate(str1):
            if b != 'T':
                continue
            size = max(pre + m - i, 0)
            # Prefix/Suffix overlap must be consistent
            if size > 0 and z[m - size] < size:
                return ""
            ans[i + size: i + m] = str2[size:]
            pre = i
            
        # Precompute nearest pending positions
        pre_q = [-1] * len(ans)
        pre = -1
        for i, c in enumerate(ans):
            if c == '?':
                ans[i] = 'a'
                pre = i
            pre_q[i] = pre
            
        # Match ans against t using Z-function
        z = calc_z(str2 + ''.join(ans))
        
        # Process 'F'
        i = 0
        while i < n:
            if str1[i] != 'F':
                i += 1
                continue
            if z[m + i] < m:
                i += 1
                continue
            # Modify the last pending position
            j = pre_q[i + m - 1]
            if j < i:
                return ""
            ans[j] = 'b'
            i = j + 1  # Optimization: skip past the modified index
        return ''.join(ans)
        