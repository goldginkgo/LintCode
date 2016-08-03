###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/strstr/

    Implement strStr(). For a given source string and a target string, 
    you should output the first index(from 0) of target string in source string.
    If target does not exist in source, just return -1.

Analysis:
    There are 2 ways to solve this problem.
    1. Most common way is to use 2 nested loop
    2. Also can be solved by KMP algorithm
"""

class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        if target == "":
            return 0
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
                if j == len(target) - 1:
                    return i
        return -1

class Solution2:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source) - len(target) + 1):
            if source[i : i + len(target)] == target:
                    return i
        return -1

class Solution_KMP:
    def strStr(self, source, target):
        # TODO
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.strStr("source", "target")
    print s.strStr("abcdabcdefg", "bcd")
    print s.strStr("abc", "bcd") # index may out of range
    print s.strStr(None, None)
    print s.strStr("", "")