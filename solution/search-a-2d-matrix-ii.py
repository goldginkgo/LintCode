###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-a-2d-matrix-ii/

    Write an efficient algorithm that searches for a value in an m x n matrix,
    return the occurrence of it.
    This matrix has the following properties:
        * Integers in each row are sorted from left to right.
        * Integers in each column are sorted from up to bottom.
        * No duplicate integers in each row or column.

    Example:
    Consider the following matrix:
    [
        [1, 3, 5, 7],
        [2, 4, 7, 8],
        [3, 5, 9, 10]
    ]
    Given target = 3, return 2.

Analysis:
    from bottom left to top right
    
"""

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return 0

        n, m = len(matrix), len(matrix[0])
        x, y = n - 1, 0
        count = 0

        while x >= 0 and y < m:
            if target > matrix[x][y]:
                y += 1
            elif target < matrix[x][y]:
                x -= 1
            else:
                count += 1
                x -= 1
                y += 1
        return count

if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([[1, 3, 5, 7], [2, 3, 7, 8], [3, 5, 9, 10]], 3)
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print s.searchMatrix(matrix, 5)
    print s.searchMatrix(matrix, 20)