###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/wood-cut/

    Given n pieces of wood with length L[i] (integer array). Cut them into 
    small pieces to guarantee you could have equal or more than k pieces with 
    the same length. What is the longest length you can get from the n pieces 
    of wood? Given L & k, return the maximum length of the small pieces.

    Example:
    For L=[232, 124, 456], k=7, return 114.

    Note:
    You couldn't cut wood into float length.

    Challenge:
    O(n log Len), where Len is the longest length of the wood.

Analysis:
    Binary search. Find the larget length that can cut more than k pieces. 
"""

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            pieces = sum([l / mid for l in L])
            if pieces >= k:
                start = mid
            else:
                end = mid

        if sum([l / end for l in L]) >= k:
            return end
        return start

if __name__ == '__main__':
    s = Solution()
    print s.woodCut([232, 124, 456], 7)
    print s.woodCut([1, 2, 3], 7)