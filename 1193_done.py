'''
问题描述：给定一个单词，你需要判断其中大写字母的使用是否正确。

当下列情况之一成立时，我们将单词中大写字母的用法定义为正确：

这个单词中的所有字母都是大写字母，如“USA”。
这个单词中的所有字母都不是大写字母，如“lintcode”。
如果它有多个字母，例如“Google”，那么这个单词中的第一个字母就是大写字母。
否则，我们定义该单词没有以正确的方式使用大写字母。

注：输入将是一个由大写和小写拉丁字母组成的非空单词。

示例：
    输入: "USA"
    输出: True

    输入: "FlaG"
    输出: False

思路：
    分以下几种情况讨论：
    1.首字母小写
        1.1后面的字母必须全小写
    2.首字母大写
        2.1后面的字母必须全大写
        2.2后面的字母必须全小写

'''


def detectCapitalUse(word):
    # write your code here
    # 判断第一个字母是大写字母还是小写字母
    start_with_capital = False
    continue_capital = False
    if ord(word[0]) >= 65 and ord(word[0]) < 97:
        start_with_capital = True
    if ord(word[1]) >= 65 and ord(word[1]) < 97:
        continue_capital = True
    for i in range(2, len(word)):
        # 首字母是小写字母的话，后面都必须是小写
        if not start_with_capital:
            if ord(word[i]) >= 97:
                continue
            else:
                return False
        # 首字母是大写字母的话，后面的字母必须全小写或或者大写
        else:
            if not continue_capital:
                if ord(word[i]) >= 97:
                    continue
                else:
                    return False
            else:
                if ord(word[i]) >= 65 and ord(word[i]) < 97:
                    continue
                else:
                    return False
    return True

if __name__ == '__main__':
    word = 'FFFFFFFFFFFFFFFFFFFFf'
    print(detectCapitalUse(word))
