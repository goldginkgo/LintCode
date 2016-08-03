###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/

    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?
    Would this affect the run-time complexity? How and why?
    Write a function to determine if a given target is in the array.

Analysis:
    We cannot do any better than O(n) as we can have n-1 identical elements and 
    the other being the target. In this case the target could be in any position. 
    Hence, traversing the array is the best we can do.
"""

class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        if len(A) == 0:
            return False
        for i in range(len(A)):
            if A[i] == target:
                return True
        return False

    def search2(self, A, target):
        for i in xrange(0, len(A)):
            if A[i]==target:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.search([4, 5, 1, 2, 3], 1)
    print s.search([4, 5, 1, 2, 3], 5)
    print s.search([4, 5, 1, 2, 3], 0)
    print s.search([], 1)
    print s.search([2,2,2,3,1], 1)