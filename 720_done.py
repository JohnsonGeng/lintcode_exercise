def rearrange(string):
    # Write your code here

    char_list = []
    sum = 0

    if not string:
        return string

    # 遍历，保存（可以优化排序，插入排序）
    for c in string:
        if ord(c) >= 65 and ord(c) <= 91:
            char_list.append(c)
        else:
            sum += int(c)

    new_str = ''.join(sorted(char_list)) + str(sum)

    return new_str


if __name__ == '__main__':
    print(rearrange('AC2BEW3'))