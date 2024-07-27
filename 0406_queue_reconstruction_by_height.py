# you may go from tallest or shortest person
# here i go from the shortest one
# since anyone may be taller than this person
# the number of person in front of him should be the accurate index of himself
# in the final queue
# repeat the logic with the next one until the final
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        ans = [None] * n
        indices = list(range(n))
        while people:
            h, k = people.pop()
            i = indices.pop(k)
            ans[i] = [h, k]
        return ans

# going from the tallest one
# it looks very neat
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        # sort the array in decreasing order of height
        # within the same height group, you would sort it in increasing order of k
        # eg: Input : [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        # after sorting: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        people.sort(key=lambda x: (-x[0], x[1]))
        for a in people:
            # Now let's start the greedy here
            # We insert the entry in the output array based on the k value
            # k will act as a position within the array
            output.insert(a[1], a)
        
        return output