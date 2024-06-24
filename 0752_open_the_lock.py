# bfs for shortest path
# there are several techniques to improve space and time as well
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_adjacent_node(node):
            node_l = [node // 1000, node // 100 % 10, node // 10 % 10, node % 10]
            node_u = [[(n + (j == i)) % 10 for j, n in enumerate(node_l)] for i in range(4)]
            node_d = [[(n - (j == i)) % 10 for j, n in enumerate(node_l)] for i in range(4)]
            return [m*1000+n*100+p*10+q for m,n,p,q in node_u + node_d]

        # there are some edge cases as well
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        target = int(target) # we convert everything into numbers for faster processing
        q = [0] # pending nodes
        v = [False] * 10000 # track visited nodes with bit vector like
        for i in set([0] + list(map(int, deadends))):
            v[i] = True

        l = 1
        while q:
            q_next = []
            for n in q:
                a = get_adjacent_node(n)
                for ai in a:
                    if ai == target: # early stopping
                        return l
                    elif not v[ai]:
                        q_next.append(ai)
                        v[ai] = True
            l += 1
            q = q_next
        
        return -1