# wow i solved a 2100 rating question
# simply trie with extra information at each node
# it is just logical
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        r = {}
        for j, w in enumerate(wordsContainer):
            t = r
            k = len(w)
            for i in range(k):
                c = w[~i]
                if c not in t:
                    t[c] = {}
                if "." not in t or len(wordsContainer[t["."]]) > k:
                    t["."] = j
                t = t[c]
            if "." not in t or len(wordsContainer[t["."]]) > k:
                t["."] = j

        ans = []
        for w in wordsQuery:
            k = len(w)
            t = r
            for i in range(k):
                c = w[~i]
                if c not in t:
                    break
                t = t[c]
            ans.append(t["."])

        return ans