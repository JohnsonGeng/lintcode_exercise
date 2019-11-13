'''
问题描述：给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。

示例：
输入: tree = {1,2,3,#,#,4,5}
输出: 3
样例解释: 树表示如下，深度是3
   1
  / \
 2   3
    / \
   4   5
它将被序列化为{1,2,3,#,#,4,5}

思路：分治法。左右子树不为空的话，返回左右子树中较高的那一个。

'''


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        self.height = self.countDepth(root)
        return self.height

    def countDepth(self, root):
        left_child_depth = 0
        right_child_depth = 0
        # 如果树为空，那么高度为0
        if not root:
            return 0
        # 如果树不为空，但是左右子树都为空，那么高度为1
        if not root.left and not root.right:
            return 1
        # 如果树不为空，且左右子树有一个不为空，那么返回二者中高度较大的一个
        if root.left or root.right:
            # 计算左子树高度
            left_child_depth = self.countDepth(root.left)
            # 计算右子树高度
            right_child_depth = self.countDepth(root.right)
            if left_child_depth > right_child_depth:
                return left_child_depth + 1
            else:
                return right_child_depth + 1