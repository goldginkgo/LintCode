###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/binary-tree-preorder-traversal/

    Given a binary tree, return the preorder traversal of its nodes' values.

    Example:
    Given binary tree {1,#,2,3}:
    1
     \
      2
     /
    3
    return [1,2,3].

Analysis:
    1. Non-recurion 2. Traverse 3. Divide & Conquer
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

#Version 0: Non-Recursion (Recommend)
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        result, stack = [], [root]
        if root is None:
            return result

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


#Version 1: Traverse (no return value)
class Solution1:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    # 把root为根的preorder加入result里面
    def traverse(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)

#Version 2: Divide & Conquer (has return value)
class Solution2:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        result = []
        # null or leaf
        if root is None:
            return result

        # Divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        # Conquer
        result.append(root.val)
        result.extend(left)
        result.extend(right)

        return result

if __name__ == '__main__':
    print Solution().preorderTraversal(None)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    print Solution().preorderTraversal(root)
