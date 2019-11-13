'''
问题描述：
给出一棵二叉树和一个整数代表树的某层深度。
计算二叉树的某层节点之和。

示例：
输入：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},2
输出：5
解释：
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
2+3=5

思路：层次遍历，记录下某层的结点和存放于列表即可


'''


def levelSum(root, level):
    # write your code here
    # 用于控制层次遍历的队列
    queue = []
    # 用于存放每层结点和的列表
    sum_list = []
    if not root:
        return 0
    queue.append(root)
    # 队列不为空
    while queue:
        sum_of_level = 0
        length = len(queue)
        for i in range(length):
            sum_of_level += queue[i].val
            # 左孩子存在则入队
            if queue[i].left:
                queue.append(queue[i].left)
            # 右孩子存在则入队
            if queue[i].right:
                queue.append(queue[i].right)
        # 截取新入队的元素
        queue = queue[length:]
        sum_list.append(sum_of_level)
    if level > len(sum_list) or level < 1:
        return 0
    else:
        return sum_list[level - 1]