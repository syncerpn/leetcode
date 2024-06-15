#1. kinda greedy: check if the current char is equal to the last char
#2. we may form the pattern s[0:i+1]
#3. then try to check various conditions
def solve(s: str) -> bool:
    n = len(s)
    for i in range(n//2):
        if s[i] == s[-1]:
            if n % (i+1) == 0:
                if s[:i+1] * (n // (i+1)) == s:
                    return True
    
    return False

#4. another solution that try to check whether s appears in its doubled string
#5. with first and last char removed; creative way
def solve2(s: str) -> bool:
    return s in (s + s)[1:-1]

#6. KMP algorithm for finding longest substring that is both prefix and suffix of a string
#7. this one took me quite a while to understand
#8. it basically uses two pointers, pi for prefix and si for suffix
#9. and uses a lps to hold information about the longest substring *up to this point*
#10. by *up to this point*, i mean the string s[0:this_point], and NOT considering the rest
#11. initially, si and pi are set to two very first characters, then increased to compare prefix and suffix substring
#12. if we find a difference chars, it resets pi to lps[pi-1]
#13. beautiful solution
def solve3(self, s: str) -> bool:
    n = len(s)
    lps = [0 for _ in range(n)]
    pi = 0 #prefix pointer
    si = 1 #suffix pointer
    while si < n:
        if s[si] == s[pi]:
            lps[si] = pi + 1
            pi += 1
            si += 1
        else:
            if pi == 0:
                si += 1
            else:
                pi = lps[pi-1]
    
    return lps[-1] > 0 and n % (n - lps[-1]) == 0