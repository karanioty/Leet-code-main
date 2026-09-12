'''94. Binary Tree Inorder Traversal
""Example:
Input: root = [1,null,2,3]
Output: [1,3,2]'''
#code link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root):
            if root is not None:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        return l
