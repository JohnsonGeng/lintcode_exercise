'''
问题描述：翻转一棵二叉树。左右子树交换。

示例：
输入: {1,2,3,#,#,4}
输出: {1,3,2,#,4}
解释:

      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4

思路：分治法。交换根节点的左右子树，如果左右子树存在，继续交换他们的左右子树。

'''

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        # 如果左右子树不为空，那么交换二者
        if root.left or root.right:
            root.left,root.right = root.right,root.left
            if root.left:
                # 左子树存在，那么递归交换左子树的左右孩子
                self.invertBinaryTree(root.left)
                # 右子树存在，那么递归交换右子树的左右孩子
            if root.right:
                self.invertBinaryTree(root.right)

