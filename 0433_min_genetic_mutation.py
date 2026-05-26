# graph traversal
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_connected(a, b):
            t = 0
            for c, d in zip(a, b):
                if c != d:
                    t += 1
                if t > 1:
                    return False
            return t == 1

        bank = set(bank)
        bank.add(startGene)
        if endGene not in bank:
            return -1
        
        g = defaultdict(list)
        for a in bank:
            for b in bank:
                if is_connected(a, b):
                    g[a].append(b)
        
        ans = [inf]
        def traverse(a, k):
            if a == endGene:
                ans[0] = min(ans[0], k)
                return
            bank.discard(a)
            for b in g[a]:
                if b not in bank:
                    continue
                traverse(b, k+1)
            bank.add(a)
        
        traverse(startGene, 0)
        return ans[0] if ans[0] < inf else -1
