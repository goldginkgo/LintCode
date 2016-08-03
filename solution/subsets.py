###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/subsets/

    Given a set of distinct integers, return all possible subsets.
    For example, If S = [1,2,3], a solution is: 
    [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]

    Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

Analysis:
    This is a DFS problem.(Backtracking)
    [], [1], [1, 2], [1, 2, 3]
    [1, 3]
    [2], [2, 3]
    [3]

"""

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        result = []
        S.sort()
        self.subsets_helper(result, [], S, 0)
        return result

    # use pos to avoid duplication
    def subsets_helper(self, result, list_temp, S, pos):
        # save previous result
        result.append(list(list_temp))

        for i in range(pos, len(S)):
            list_temp.append(S[i])
            self.subsets_helper(result, list_temp, S, i + 1)  # not pos + 1
            list_temp.pop()

# For other solutions, refer to the following links.
# http://www.cnblogs.com/yuzhangcmu/p/4211815.html
# http://www.shuatiblog.com/blog/2014/05/22/Subsets/

if __name__ == "__main__":
    s = Solution()
    print s.subsets([1,2,3])
    print s.subsets([4,1,0])