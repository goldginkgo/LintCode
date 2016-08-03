###############################################################################
"""
Question:
    LintCode: http://www.jiuzhang.com/solutions/minimum-depth-of-binary-tree/

    The minimum depth is the number of nodes along the shortest path from the 
    root node down to the nearest leaf node.

    Example:
    Given a binary tree as follow:
            1

         /     \ 

       2        3

              /    \

            4       5  

    The minimum depth is 2


Analysis:
    Divide & Conquer
"""

import sys
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        if root is None:
            return 0

        return self.getMin(root)

    def getMin(self, root):
        if root is None:
            return sys.maxint

        if root.left is None and root.right is None:
            return 1

        return min(self.getMin(root.left), self.getMin(root.right)) + 1

    def minDepth2(self, root):
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1
        return min(left, right) + 1

    def minDepth3(self, root):
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

if __name__ == '__main__':
    print Solution().minDepth(None)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print Solution().minDepth(node1)
