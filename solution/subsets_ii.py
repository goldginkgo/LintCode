###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/subsets-ii/

    Given a list of numbers that may has duplicate numbers, return all possible
    subsets. For example, If S = [1,2,2], a solution is: 
    [ [2], [1], [1,2,2], [2,2], [1,2], [] ] 

    Note:
    Each element in a subset must be in non-descending order.
    The ordering between two subsets is free.
    The solution set must not contain duplicate subsets.

Analysis:
    This is a DFS problem.(Backtracking)
    It is similar to subsets.py.
"""

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        result = []
        S.sort()
        self.subsets_helper(result, [], S, 0)
        return result

    # use pos to avoid duplication
    def subsets_helper(self, result, list_temp, S, pos):
        # save previous result
        result.append(list(list_temp))

        for i in range(pos, len(S)):
            if i != pos and S[i] == S[i - 1]:
                continue
            list_temp.append(S[i])
            self.subsets_helper(result, list_temp, S, i + 1)  # not pos + 1
            list_temp.pop()


if __name__ == "__main__":
    s = Solution()
    print s.subsetsWithDup([1,2,2])