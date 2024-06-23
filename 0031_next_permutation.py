# iterate backward, finding the turning point where the iterating first decreases after continuous increasing
# we swap the anchor with its next higher one within the increasing array
# reverse that increasing array
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n > 1:
            t = nums[0]
            for i in range(n-1, 0, -1):
                a = nums[i-1]
                b = nums[i]
                if a < b:
                    t = a
                    break
            else:
                i = 0
            
            print(i)
            if i > 0:
                for j in range(n-1, i-1, -1):
                    if nums[j] > t:
                        a = nums[j]
                        nums[j] = nums[i-1]
                        nums[i-1] = a
                        break
            
            j = i
            k = n-1
            while k > j:
                a = nums[j]
                nums[j] = nums[k]
                nums[k] = a
                
                k -= 1
                j += 1