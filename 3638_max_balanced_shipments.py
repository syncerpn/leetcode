# "parcels may remain unshipped", lol
# that means, you dont have to put every parcel in a shipment
# i.e. you may skip some number in the array
# so just use greedy
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        m, i, n = 0, 1, len(weight)
        ans = 0
        while i < n and m < n:
            if weight[i] < weight[m]:
                ans += 1
                m = i + 1
                i += 2
            else:
                m = i
                i += 1
        return ans

# dont even need to track max
# just pair them and make sure weight[i+1] < weight[i] for one shipment
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        i, n = 0, len(weight)
        ans = 0
        while i < n - 1:
            if weight[i+1] < weight[i]:
                ans += 1
                i += 1
            i += 1
        return ans