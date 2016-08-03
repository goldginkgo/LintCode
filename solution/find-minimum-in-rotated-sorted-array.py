###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.

    Example
        Given [4, 5, 6, 7, 0, 1, 2] return 0
    
    Note
        You may assume no duplicate exists in the array.

Analysis:
    Binary search. Find the first element <= target 
"""

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        if len(num) == 0:
            return 0

        start, end = 0, len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] <= num[-1]:
                end = mid
            else:
                start = mid
        # return min(num[start], num[end])
        if num[start] <= num[-1]:
            return num[start]
        else:
            return num[end]

if __name__ == '__main__':
    s = Solution()
    print s.findMin([6,1,2,3,4,5])
    print s.findMin([1,2,3])
    print s.findMin([])