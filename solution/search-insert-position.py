###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-insert-position/

    Given a sorted array and a target value, return the index if the target is 
    found. If not, return the index where it would be if it were inserted in 
    order. You may assume NO duplicates in the array.

    Example
        [1,3,5,6], 5 -> 2
        [1,3,5,6], 2 -> 1
        [1,3,5,6], 7 -> 4
        [1,3,5,6], 0 -> 0
Analysis:
    Binary search. 
    Find the first position >= target or 
    Find the last position < target, return +1
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        elif A[end] >= target:
            return end
        else:
            return end + 1

if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
    print s.searchInsert([], 9)