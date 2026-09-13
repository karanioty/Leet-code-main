'''145. Binary Tree Postorder Traversal
""Example:
Input: root = [1,null,2,3]
Output: [3,2,1]'''
#code link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(root):
            if root is not None:
                postorder(root.left)
                postorder(root.right)
                l.append(root.val)
        postorder(root)
        return l
