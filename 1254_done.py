'''
问题描述：找出给定二叉树中，所有左叶子的值之和。
示例：
输入：
{3,9,20,#,#,15,7}
输出：24

解释：这棵二叉树中，有两个左叶子结点，它们的值分别为9和15。因此返回24。
    3
   / \
  9  20
    /  \
   15   7
思路：递归找出叶子结点，累计添加权值即可
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """

    def sumOfLeftLeaves(self, root):
        # Write your code here
        # 思路：递归找出叶子结点，累计添加权值即可
        self.value = 0
        self.findLeaves(root)
        return self.value

    def findLeaves(self, root):
        if not root:
            return
        # 左叶子结点,累加权值
        if root.left and not root.left.left and not root.left.right:
            self.value += root.left.val
        self.findLeaves(root.left)
        self.findLeaves(root.right)