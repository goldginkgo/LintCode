###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    The array may contain duplicates.

    Example
        Given [4,4,5,6,7,0,1,2] return 0

Analysis:
    It can not be solved by Binary search.
    [1,1,..., 1] with only one 0 in it
    It ends up the same as sequential search
    We used linear search for this question just to indicate that the time 
    complexity of this question is O(n) regardless of binary search is applied or not.
"""
class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        if len(num) == 0:
            return -1
        ret = num[0]
        for i in range(len(num) - 1):
            if num[i] < ret:
                ret = num[i]
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.findMin([6,1,2,3,4,5])
    print s.findMin([1,2,3])
    print s.findMin([4,4,5,6,7,0,1,2] )
    print s.findMin([])