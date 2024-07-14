# very good problem actually
# should be rated "medium" or "hard"
# the point is to keep track of minimal vowel substrings
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        VOWELS = set("aeiou")
        r = 0
        v, s, j, ri = {c: 0 for c in VOWELS}, set(), 0, 1
        for i, c in enumerate(word):
            if c not in VOWELS:
                # when a consonant is encountered
                # it is a new start
                v, s, j, ri = {c: 0 for c in VOWELS}, set(), i+1, 1
            else:
                s.add(c)
                v[c] += 1
                # we keep counting vowels appeared in the current substring
                if s == VOWELS:
                    # this step, we try to keep track of the minimal substring
                    # then as we found a new vowel,
                    # we can form one vowel substring from it and the minimal substring
                    # and any vowel before it (up to the next consonant)
                    while v[word[j]] > 1:
                        v[word[j]] -= 1
                        ri += 1
                        j += 1
                    # add the count of formable vowel substrings to final result
                    r += ri
        
        return r