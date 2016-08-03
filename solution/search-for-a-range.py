###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-for-a-range/

    Given a sorted array of n integers, find the starting and ending position 
    of a given target value. If the target is not found in the array, return 
    [-1, -1].

    Example:
    Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

Analysis:
    Find the left bound and right bound with binary search.
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]

        bound = [-1, -1]
        # left bound
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            bound[0] = start
        elif A[end] == target:
            bound[0] = end
        else:
            bound[0] = bound[1] = -1
            return bound

        # right bound
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid    ##
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            bound[1] = end  ##
        elif A[start] == target:
            bound[1] = start
        else:
            bound[0] = bound[1] = -1
            return bound

        return bound

if __name__ == "__main__":
    s = Solution()
    print s.searchRange([5, 7, 7, 8, 8, 10], 8)
    print s.searchRange([5, 5, 5, 5, 5, 5], 5)
    print s.searchRange([1, 2, 3, 4, 5, 6], 7)