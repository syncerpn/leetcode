# sorting is trivial
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        return sum(arr[n//20:-n//20]) / (n * 18 // 20)

# how about using quick-select, which is O(n) (refer to #0215)
# also heap with fixed size will work
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        def findKthLargest(nums: List[int], k: int) -> int:
            # we keep filtering out some values in nums until we find kth
            while nums:
                l = []
                r = []
                m = 0

                # choose a random pivot is better than fixed one
                pivot = random.choice(nums)
                
                # now do partitioning
                for n in nums:
                    if n > pivot:
                        r.append(n)
                    elif n < pivot:
                        l.append(n)
                    else:
                        m += 1
                
                # and then detect which partition to be considered next
                if len(r) < k <= len(r) + m:
                    return pivot
                elif len(r) >= k:
                    nums = r
                else:
                    nums = l
                    k -= m + len(r)
    
        n = len(arr)
        a_small = findKthLargest(arr, 19 * n // 20 + 1)
        a_large = findKthLargest(arr,  1 * n // 20)
        n_small = n // 20
        n_large = n // 20
        
        s = 0
        for a in arr:
            if a < a_small:
                n_small -= 1
            elif a > a_large:
                n_large -= 1
            else:
                s += a
        
        return (s - n_small * a_small - n_large * a_large) / (18 * n // 20)