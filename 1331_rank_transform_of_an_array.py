# this one does not use hashmap
# instead, index sorting based on value
# pretty nice problem though its tag is easy
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        indices = list(range(1, len(arr)+1))
        sorted_indices = sorted(indices, key=lambda x: arr[x-1])
        c = 0
        for i in range(1, len(arr)):
            if arr[sorted_indices[i]-1] == arr[sorted_indices[i-1]-1]:
                c += 1
            indices[i] -= c

        rank = [0] * len(arr)
        for i, j in enumerate(sorted_indices):
            rank[j-1] = indices[i]
        return rank

# replay this in potd
# make it compact
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {a: i+1 for i, a in enumerate(sorted(list(set(arr))))}
        return [d[a] for a in arr]