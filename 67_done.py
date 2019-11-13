'''
问题描述：给出一棵二叉树,返回其中序遍历

示例：
输入：{1,#,2,3}
输出：[1,3,2]
解释：
1
 \
  2
 /
3
它将被序列化为{1,#,2,3}
中序遍历

思路：递归实现即可

'''

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.output = []
        self.traverse(root)
        return self.output

    def traverse(self,node):
        if node != None:
            self.traverse(node.left)
            self.output.append(node.val)
            self.traverse(node.right)
        return 