#1. string manip O(NM) should work
def solve(dictionary: list, sentence: str) -> str:
    words = sentence.split(" ")
    for i in range(len(words)):
        for root in dictionary:
            if words[i].startswith(root):
                words[i] = root
    
    return " ".join(words)

#1. using Trie data structure could speed up processing
def solve(dictionary: list, sentence: str) -> str:
    def add_node(k: str, d: dict) -> dict: #add key k to dict d; return d[k] as dict
        if k not in d:
            d[k] = {}
        return d[k]

    trie = {}
    for root in dictionary:
        t = trie
        n = len(root)
        for i, c in enumerate(root):
            if i == n-1:
                t[c] = None
                break
            t = add_node(c, t)
            if t is None:
                break

    words = sentence.split(" ")
    for i, word in enumerate(words):
        t = trie
        r = ""
        for c in word:
            if c in t:
                t = t[c]
                r += c
            else:
                break
            
            if t is None:
                words[i] = r
                break
    
    return " ".join(words)