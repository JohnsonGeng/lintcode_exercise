'''
问题描述：输入一个英文句子，将每个单词的第一个字母改成大写字母
思路：循环扫描字符串加入列表，遇到某个字符前面是空格的，便将其变大写。

'''
def capitalizesFirst(s):
    # Write your code here
    index = 0
    list = []
    while index <= len(s ) -1:
        # 单独处理第一个元素
        if index == 0:
            if s[index] != ' ':
                list.append(chr(ord(s[index] ) -32))
            else:
                list.append(s[index])
        # 后面的元素
        else:
            # 说明是某个单词中的字符
            if s[index] != ' ' and s[index -1] != ' ':
                list.append(s[index])
            elif s[index] != ' ' and s[index -1] == ' ':
                list.append(chr(ord(s[index] ) -32))
            else:
                list.append(s[index])
        index += 1
    return ''.join(list)

if __name__ == '__main__':
    s = "i want to get an accepted"
    print(capitalizesFirst(s))