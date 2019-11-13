'''
问题描述：给出一棵二叉树，
返回其节点值从底向上的层次序遍历（
按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）

示例：
输入:
{3,9,20,#,#,15,7}
输出:
[[15,7],[9,20],[3]]
解释:
    3
   / \
  9  20
    /  \
   15   7
它将被序列化为 {3,9,20,#,#,15,7}
层次遍历

思路：正常层次遍历即可。最后将结果列表逆序，或者利用栈处理即可。

'''

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        queue = []
        result_list = []
        # 根节点为空，那么返回空表
        if not root:
            return result_list
        queue.append(root)
        while queue:
            # 存放当前层的结点
            cur_level_list = []
            length = len(queue)
            for i in range(length):
                cur_level_list.append(queue[i].val)
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            result_list.append(cur_level_list)
            queue = queue[length:]
        result_list.reverse()
        return result_list