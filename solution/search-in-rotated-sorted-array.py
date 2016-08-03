###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    You are given a target value to search. If found in the array return its 
    index, otherwise return -1.
    You may assume no duplicate exists in the array.

    Example:
    For [4, 5, 1, 2, 3] and target=1, return 2.
    For [4, 5, 1, 2, 3] and target=0, return -1.

Analysis:
    Binary search. 

                 /|
               M/ |
 (situation 1) /  |
              /   |
            S/    |
                  |   
      ------------|-------------
                  | 
                  |      /E
                  |     /
                  |    / (situation 2)
                  |   /M'  
                  |  /    
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[mid] > A[start]:  # decide where middle is
                # situation 1, numbers between start and mid are sorted
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # situation 2, numbers between mid and end are sorted
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.search([4, 5, 1, 2, 3], 1)
    print s.search([4, 5, 1, 2, 3], 5)
    print s.search([4, 5, 1, 2, 3], 0)
    print s.search([], 1)