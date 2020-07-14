def removeDuplicateLetters(s):
    # write your code here

    count_list = {}
    result = []

    # 首先遍历字符串，记录每个元素的个数
    for c in s:
        if count_list.get(c):
            count_list[c] += 1
        else:
            count_list[c] = 1

    # 遍历数组，确定最优解
    for c in s:
        # 如果result中存在该元素，那么继续
        if c in result:
            continue
        while (result and ord(c) < ord(result[-1]) and count_list[c] != 0):
            result.pop()
        result.append(c)
        count_list[c] -= 1
        if count_list[c] == 1:
            result.pop()
            result.append(c)
            count_list[c] -= 1

    # 拼接
    new_s = ''.join(result)

    return new_s

if __name__ == '__main__':
    print(removeDuplicateLetters('cbacdcbc'))