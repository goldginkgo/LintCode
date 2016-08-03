###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-in-a-big-sorted-array/

    Given a big sorted array, find the first index of a target number. Your 
    algorithm should be in O(log k), where k is the first index of the target 
    number. Return -1, if the number doesn't exist in the array.

    Example
    Given [1, 3, 6, 9, 21], and target = 3, return 1.
    Given [1, 3, 6, 9, 21], and target = 4, return -1.

Analysis:
    Binary search.
"""

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, A, target):
        if A is None or len(A) == 0:
            return -1

        # 0 1 3 7 15 ... 2^n-1
        end = 0
        while end < len(A) and A[end] < target:  # O(log k)
            end = end * 2 + 1

        if end >= len(A):
            end = len(A) - 1

        # find first position of target
        start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1