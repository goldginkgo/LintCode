###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/find-peak-element/

    There is an integer array which has the following features:
        The numbers in adjacent positions are different.
        A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
    We define a position P is a peek if:
    A[P] > A[P-1] && A[P] > A[P+1]
    Find a peak element in this array. Return the index of the peak.
    Example
        Given [1, 2, 1, 3, 4, 5, 7, 6]
        Return index 1 (which is number 2) or 6 (which is number 7)
    Note
        The array may contains multiple peeks, find any of them.

Analysis:
    Binary search. There are 4 conditions in mid, mid - 1, mid + 1
    < <
    > >
    < >
    > <
"""

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # To ensure not out of index
        start, end = 0, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] < A[end]:
            return end
        else:
            return start