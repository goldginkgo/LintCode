###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/first-position-of-target/

    For a given sorted array (ascending order) and a target number, find the
    first index of this number in O(log n) time complexity. If the target 
    number does not exist in the array, return -1.

    Example:
    If the array is [1, 2, 3, 3, 4, 5, 10], 
    for given target 3, return 2.

Analysis:
    Two basic steps:
    1. restrict range to two numbers
    2. decide which of the two numbers is target
    Four factors of binary search.
    1. start + 1 < end
       To avoid infinite loop.
       When  start = 1, end = 2, start = mid,
       start < end will run into a infinite loop
    2. start + (end - start) / 2
       To avoid out of range when numbers are too big.
    3. A[mid] ==, <, >
    4. A[start] A[end] ? target
"""

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                end = mid  # should not return to find first
            elif nums[mid] < target:
                start = mid  # mid + 1 is also ok
            else:
                end = mid  # mid - 1 is also ok

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.binarySearch([1, 2, 3, 3, 4, 5, 10], 3)
    print s.binarySearch([1, 2, 3, 3, 4, 5, 10], 6)