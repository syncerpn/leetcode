# try using two pointers
# inplace swap position such that a number should be place at its value-1 (nums[i] == i+1)
# junk numbers (too big or negative ones) put to the end
# iterate one more time for checking any out-of-place numbers; return that one
# if there is none out-of-place, return the next integer to be in the sequence
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            n = nums[i]
            if n != i+1:
                if n > j+1 or n <= 0:
                    nums[i] = nums[j]
                    nums[j] = n
                    j -= 1
                else:
                    if nums[i] != nums[n-1]:
                        nums[i] = nums[n-1]
                        nums[n-1] = n
                    else:
                        i += 1
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return i+2

# O(1) space, O(n) time
# brilliant point is to store additional information into the array
# without losing existing information
# just by % operator
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        # delete those useless elements
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        # use the index as the hash to record the frequency of each number
        for i in range(len(nums)):
            nums[nums[i] % n] += n

        for i in range(1,len(nums)):
            if nums[i] // n == 0:
                return i
        return n