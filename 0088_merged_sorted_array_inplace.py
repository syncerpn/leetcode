#1. simple approach
def solve(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1s = sorted(nums1[:m])
    nums2s = sorted(nums2)

    mi = 0
    ni = 0
    for i in range(m+n):
        if mi < m and ni < n:
            if nums2s[ni] > nums1s[mi]:
                nums1[i] = nums1s[mi]
                mi += 1
            else:
                nums1[i] = nums2s[ni]
                ni += 1
        elif mi >= m:
            nums1[i] = nums2s[ni]
            ni += 1
        elif ni >= n:
            nums1[i] = nums1s[mi]
            mi += 1

#1. pure inplace, no extra mem, merge from last to first because empty space is at the end
def solve(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[i+j+1] = nums1[i]
            i -= 1
        else:
            nums1[i+j+1] = nums2[j]
            j -= 1
    else:
        if i < 0:
            while j >= 0:
                nums1[j] = nums2[j]
                j -= 1