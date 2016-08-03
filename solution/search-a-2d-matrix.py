###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/search-a-2d-matrix/

    Write an efficient algorithm that searches for a value in an m x n matrix.
    This matrix has the following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the
          previous row.

    Example:
    Consider the following matrix:
    [
        [ 1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    Given target = 3, return true.

Analysis:
    Binrary search. 
    Find the last row where the first number <= target
"""

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):  # Binary Search Twice
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        row = len(matrix)
        column = len(matrix[0])

        # find the row index, the last number <= target 
        start, end = 0, row - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False

        # find the column index, the number equal to target
        start, end = 0, column - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[row][start] == target:
            return True
        if matrix[row][end] == target:
            return True
        return False

    def searchMatrix2(self, matrix, target):  # Binary Search Once
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        row, column = len(matrix), len(matrix[0])
        start, end = 0, row * column - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            x, y = mid / column, mid % column
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                start = mid
            else:
                end = mid
        if matrix[start / column][start % column] == target:
            return True
        if matrix[end / column][end % column] == target:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    print s.searchMatrix2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7)
    print s.searchMatrix2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 22)
    print s.searchMatrix2([], 1)