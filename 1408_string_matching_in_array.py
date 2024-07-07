# trie solution
# solving this makes me remember trie for life lol
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def add_node(k: str, d: dict) -> dict:
            if k not in d:
                d[k] = {}
            return d[k]
        
        def find(word: str, d: dict) -> bool:
            for c in word:
                if c not in d:
                    return False
                d = d[c]
            return True
                        
        r = []
        trie = {}
        # we sort the word list by length in descending order
        # we will build trie from longest word and check if any following words are substring of built words
        for word in sorted(words, key=lambda x: len(x), reverse=True):
            if find(word, trie):
                r.append(word)
            
            # there is nothing fancy, we just build trie from each word and its every substring
            # this is O(k2) where k is length of word
            for i in range(len(word)):
                t = trie
                for c in word[i:]:
                    t = add_node(c, t)
        return r

# simpler, yet O(n2)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = " ".join(words)
        return [word for word in words if s.count(word) > 1]