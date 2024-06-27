# quite nice problem
# we need to find k-star subgraph
# remember its k-star
# so we will use priority queue to keep track of at most k largest adjacent nodes of each node
# skip negative-value adjacent nodes as well
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        s_max = max(vals)
        if k == 0:
            return s_max

        # keep track of k best adjacent nodes here in d
        d = {i:[] for i in range(len(vals))}
        for a, b in edges:
            # skip those negative ones
            if vals[b] > 0:
                # keep pushing in
                if len(d[a]) < k:
                    heapq.heappush(d[a], vals[b])
                # until the number of nodes is k
                # then consider popping the smaller and pushing the bigger
                elif vals[b] > d[a][0]:
                    heapq.heappop(d[a])
                    heapq.heappush(d[a], vals[b])

            # repeat with the other node on the same edge
            if vals[a] > 0:
                if len(d[b]) < k:
                    heapq.heappush(d[b], vals[a])
                elif vals[a] > d[b][0]:
                    heapq.heappop(d[b])
                    heapq.heappush(d[b], vals[a])

        # finally find the max sum
        for i in d:
            s_max = max(s_max, vals[i] + sum(d[i]))

        return s_max