# pivot quicksort in-place O(1) space
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def pivot(nums, a, b):
            if a < b:
                i, j = a, b
                p = nums[random.randint(i, j)]
                r, m = a, a
                for n in nums[i:j+1]:
                    if n < p:
                        m += 1
                        r += 1
                    elif n == p:
                        r += 1
                k = m
                while i < m or j >= r:
                    if i < m and nums[i] < p:
                        i += 1
                    elif j >= r and nums[j] > p:
                        j -= 1
                    elif i < m and nums[i] == p:
                        nums[i], nums[k] = nums[k], nums[i]
                        k += 1
                    elif j >= r and nums[j] == p:
                        nums[j], nums[k] = nums[k], nums[j]
                        k += 1
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1
                pivot(nums, a, m-1)
                pivot(nums, r, b)
        
        pivot(nums, 0, len(nums)-1)
        return nums