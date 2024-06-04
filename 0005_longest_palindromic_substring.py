#1. iterate the string
#2. find palindrome by extending from the center, where the current char is the center
#3. pay attention to removing all char same as the center ("zcccccz" case for example)
def solve(s: str) -> str:
    max_p_length = 1
    max_p_i = [0,0]

    i = 0
    while i < len(s):
        n = 1
        l = i - 1
        r = i + 1
        c = s[i]
        while l >= 0:
            if s[l] != c:
                break
            
            l = l - 1
        
        while r < len(s):
            if s[r] != c:
                break
            
            r = r + 1
        
        i = r

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l = l - 1
            r = r + 1
        
        if (r - l - 1) > max_p_length:
            max_p_i = [l+1,r-1]
            max_p_length = r - l - 1
        
    l, r = max_p_i
    return s[l:r+1]