# my trie solution
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def get_product(n, k):
            ans = []
            for c in n:
                if k <= 0:
                    break
                if c == ".":
                    ans.append("")
                    k -= 1
                else:
                    t = get_product(n[c], k)
                    t = [c + ti for ti in t[:k]]
                    ans += t
                    k -= len(t)
            return ans
                

        r = OrderedDict()
        for p in sorted(products):
            n = r
            for c in p:
                if c not in n:
                    n[c] = {}
                n = n[c]
            n["."] = None
        
        ans = []
        n = r
        p = ""
        for c in searchWord:
            if c in n:
                p += c
                ans.append([p + ti for ti in get_product(n[c], 3)])
                n = n[c]
            else:
                ans.append([])
                n = {}

        return ans

# someone solved it with sort and binary search
# somehow this is super fast
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        low = 0
        for char in searchWord:
            prefix += char
            low = bisect_left(products, prefix, low)
            search_result = []
            for product in products[low:low + 3]:
                if product.startswith(prefix):
                    search_result.append(product)
            result.append(search_result)
        return result