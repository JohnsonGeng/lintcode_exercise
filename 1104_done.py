'''
问题描述：
最初，机器人位于(0, 0)处。
给定一系列动作，判断该机器人的移动轨迹是否是一个环，这意味着它最终会回到原来的位置。
移动的顺序由字符串表示。
每个动作都由一个字符表示。 有效的机器人移动是R（右），L（左），U（上）和D（下）。
输出应该为true或false，表示机器人是否回到原点。

示例：
输入: "UD"
输出: true

思路：
定义x与y，初始值为0，0。根据上下左右修改x和y的值即可



'''

class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        # 思路：定义x与y，初始值为0，0。根据上下左右修改x和y的值即可
        x = 0
        y = 0
        for move in moves:
            if move == 'R':
                x += 1
            if move == 'L':
                x -= 1
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False