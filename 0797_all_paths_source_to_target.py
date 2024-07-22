# recursive next node to target
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(i, graph, target):
            if i == target:
                return [[target]]

            result = []
            for j in graph[i]:
                paths = helper(j, graph, target)
                for p in paths:
                    result.append([i] + p)
            
            return result
        return helper(0, graph, len(graph)-1)