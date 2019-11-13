'''
问题描述：给定二叉树，返回它是否是自身的镜像（即这棵二叉树是否对称）。

示例：
输入: {1,2,2,3,4,4,3}
输出: true
解释:
    1
   / \
  2   2
 / \ / \
3  4 4  3
{1,2,2,3,4,4,3}这棵二叉树是对称的

思路：如果中序遍历得到的序列是对称的，那么这颗二叉树就是对称的

'''


class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """

    def isSymmetric(self, root):
        # Write your code here
        # 思路：中序遍历的序列是对称的！
        self.result = []
        self.traverse(root)
        self.result_reversed = self.result[::-1]
        if self.result == self.result_reversed:
            return True
        else:
            return False

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.result.append(root.val)
            self.traverse(root.right)