# concise solution with trie
# copied from others
# the idea is keep inserting char pairs of a word and its reversed as if it is prefix and suffix
# when encountered an ending sign, we know we encounter a word in words
# count it as one pair
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = (T := lambda: defaultdict(T))()
        res = 0
        for w in words:
            x = root
            for k in zip(w, reversed(w)):
                res += (x := x[k]).get(0, 0)
            x[0] = x.get(0, 0) + 1
        return res