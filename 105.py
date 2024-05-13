# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        # 找到左子树中结点的个数
        left_num = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: 1+left_num], inorder[:left_num])
        root.right = self.buildTree(preorder[1+left_num:], inorder[left_num+1:])
        return root
