'''
问题描述：
翻转游戏：给定一个只包含两种字符的字符串：+和-，你和你的小伙伴轮流翻转"++"变成"--"。当一个人无法采取行动时游戏结束，另一个人将是赢家。

编写一个函数，计算字符串在一次有效移动后的所有可能状态。

示例：
输入: s = "++++"
输出:
[
  "--++",
  "+--+",
  "++--"
]

思路：扫描字符串，将相邻的两个"++"变成"=="即可


'''


def generatePossibleNextMoves(s):
    # write your code here
    i = 0
    result_list = []
    temp_str1 = ''
    temp_str2 = ''
    while i <= len(s) - 2:
        # 查看是否有相邻的两个‘+’号，有则变成‘-’，加入result列表
        if s[i] == '+' and s[i+1] == '+':
            temp_str1 = s[:i]
            temp_str2 = s[i + 2:]
            result_list.append(temp_str1 + '--' + temp_str2)
        else:
            i += 1
            continue
        i += 1
    return result_list

if __name__ == '__main__':
    s = "---+++-+++-+"
    print(generatePossibleNextMoves(s))