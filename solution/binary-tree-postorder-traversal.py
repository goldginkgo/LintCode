###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/

    Given a binary tree, return the postorder traversal of its nodes' values.

    Example:
    Given binary tree {1,#,2,3}:
    1
     \
      2
     /
    3
    return [3,2,1].

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        result.extend(left)
        result.extend(right)
        result.append(root.val)

        return result

    # Iterative -- rather difficult to understand!!!
    # http://www.shuatiblog.com/blog/2014/06/03/Binary-Tree-Postorder-Traversal/
    def postorderTraversal2(self, root):
        result, stack = [], []
        prev = None  # previously traversed node

        if root is None:
            return result

        stack.append(root)
        while stack:
            curr = stack[-1]
            if prev is None or prev.left == curr or prev.right == curr:
                # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif prev == curr.left:
                # traverse up the tree form the left
                if curr.right:
                    stack.append(curr.right)
            else:
                # prev == curr.right or prev == curr
                # traverse up the tree from the right
                # or at a leaf node
                result.append(curr.val)
                stack.pop()
            prev = curr
        return result

    # To get postorder(left->right->root), we just need to reverse the result
    # of (root->right->left)
    # A little modification of preorder(root->left->right) is enough.
    def postorderTraversal3(self, root):
        result, stack = [], [root]

        if root is None:
            return result

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()          
        return result

    # When to pop a node from stack: 1. has no child 2.children are visited
    def postorderTraversal4(self, root):
        result, stack = [], [root]
        prev = None

        if root is None:
            return result

        while stack:
            curr = stack[-1]
            no_child = curr.left is None and curr.right is None
            # prev was initialized to None
            child_visited = prev and (curr.left == prev or curr.right == prev)
            if no_child or child_visited:
                result.append(curr.val)
                stack.pop()
                prev = curr
            else:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

        return result

    def postorderTraversal5(self, root):
        result, stack, curr, prev = [], [], root, None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                parent = stack[-1]
                if parent.right in (None, prev):
                    result.append(parent.val)
                    prev = stack.pop()
                else:
                    curr = parent.right
        return result

if __name__ == '__main__':
    print Solution().postorderTraversal5(None)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    print Solution().postorderTraversal5(root)