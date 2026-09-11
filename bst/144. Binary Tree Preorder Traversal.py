'''144. Binary Tree Preorder Traversal
""Example:
Input: root = [1,null,2,3]
Output: [1,2,3]'''
#code link: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def value(root):
            if root is not None:
                l.append(root.val)
                value(root.left)
                value(root.right)
        value(root)
        return l
