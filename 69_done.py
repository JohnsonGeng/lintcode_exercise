'''
问题描述：
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）。

示例：
输入：{1,2,3}
输出：[[1],[2,3]]
解释：
   1
  / \
 2   3
它将被序列化为{1,2,3}
层次遍历

思路：层次遍历，在循环内部用一个列表来存放

'''

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        # 用于控制层次遍历的队列
        queue = []
        # 用于存放结果的列表
        result_list = []
        # 如果是空表则返回空列表
        if not root:
            return result_list
        # 根结点入队
        queue.append(root)
        # 当队列不为空的时候
        while queue:
            level_list = []
            length = len(queue)
            for i in range(length):
                level_list.append(queue[i].val)
                # 左孩子不为空，那么左孩子入队
                if queue[i].left:
                    queue.append(queue[i].left)
                # 右孩子不为空，那么右孩子入队
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[length:]
            result_list.append(level_list)
        return result_list
