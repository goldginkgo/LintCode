###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/

    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
    Given binary tree {1,#,2,3}:
    1
     \
      2
     /
    3
    return [1,3,2].

Analysis:
    Divide & Conquer
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)
        return result

    def inorderTraversal2(self, root):
        result, stack, current = [], [], root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

    def inorderTraversal3(self, root):
        result, stack, current = [], [], root
        while current:
            stack.append(current)
            current = current.left

        while stack:
            current = stack.pop()
            result.append(current.val)
            current = current.right
            while current:
                stack.append(current)
                current = current.left
        return result

if __name__ == '__main__':
    print Solution().inorderTraversal2(None)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    print Solution().inorderTraversal2(root)
