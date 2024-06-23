# we will use dict to lookup words as we slide through the given string
# the point is to keep track of the number of words appeared and adjust the sliding window accordingly
# this implementation tracks index; it is ok to track only number of occurences that when necessary, go back and remove invalid yet seen words during a sliding iter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        m = len(words)
        n = len(s)

        if k * m > n:
            return []
        
        result = []
        
        d = {}
        for i, word in enumerate(words):
            if word not in d:
                d[word] = 0
            d[word] += 1

        for j in range(k):
            slice_d = {}
            slice_d_len = 0
            slice_d_ans = j
            for i in range(j,n,k):
                slice_s = s[i:i+k]
                if slice_s not in d:
                    slice_d = {}
                    slice_d_len = 0
                    slice_d_ans = i+k
                else:                    
                    if slice_s not in slice_d:
                        slice_d[slice_s] = []
                    
                    for p in range(len(slice_d[slice_s])-1,-1,-1):
                        if slice_d[slice_s][p] < slice_d_ans:
                            slice_d[slice_s] = slice_d[slice_s][p+1:]
                            break
                            
                    if len(slice_d[slice_s]) == d[slice_s]:
                        slice_d_len -= (slice_d[slice_s][0] - slice_d_ans) // k + 1
                        slice_d_ans = slice_d[slice_s][0] + k
                        slice_d[slice_s] = slice_d[slice_s][1:]
                    
                    slice_d[slice_s].append(i)
                    slice_d_len += 1
                    if slice_d_len == m:
                        result.append(slice_d_ans)
                        first_word = s[slice_d_ans:slice_d_ans+k]
                        slice_d[first_word] = slice_d[first_word][1:]
                        slice_d_len -= 1
                        slice_d_ans += k
                    
        return result