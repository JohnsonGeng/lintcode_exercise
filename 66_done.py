'''
问题描述：给出一棵二叉树，返回其节点值的前序遍历。

示例：
输入：{1,#,2,3}
输出：[1,2,3]
解释：
1
 \
  2
 /
3
它将被序列化为{1,#,2,3}
前序遍历

思路：递归遍历即可

'''


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        # 用于存储结点
        self.output = []
        # 对根节点递归调用遍历 
        self.traverse(root)
        return self.output

    def traverse(self, node):
        if node != None:
            self.output.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)
        return