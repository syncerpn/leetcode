# count one list, then verify by the other
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i, w in enumerate(list1):
            d[w] = i
        
        index_sum = None
        commons = []
        for i, w in enumerate(list2):
            if w in d: 
                if index_sum == i + d[w]:
                    commons += [w]
                elif index_sum is None or index_sum > i + d[w]:
                    index_sum = i + d[w]
                    commons = [w]
        
        return commons