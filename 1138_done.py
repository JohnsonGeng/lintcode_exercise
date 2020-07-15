'''

问题描述：
假设你有一个长花圃，其中有些地块已经被种植了，但是有些地块没有。
但是，花不能够在相邻的地块下种植，他们会争夺水从而导致两者的死亡。
给定一个花圃（用一个包含0和1的数组来表示，其中0代表空，1代表非空），
和一个数字n，返回n朵新的花在这个花圃上以能否在不违反“无相邻花”的规则种植。

示例：
Input : flowerbed = [1,0,0,0,1], n = 1
Output : True

'''


def canPlaceFlowers(flowerbed, n):
    # Write your code here

    # 特殊情况
    if n == 0 or (flowerbed == [0] and n == 1):
        return True

    # 提示前面已经有花
    before_one = False

    # 遍历数组
    for i in range(len(flowerbed)):
        # 花种完了
        if n == 0:
            return True
        else:
            if flowerbed[i] == 1:
                before_one = True
                continue
            else:
                # 前面没花，后面也没花
                if i < len(flowerbed) - 1 and flowerbed[i + 1] == 0 and not before_one:
                    n -= 1
                    before_one = True
                else:
                    before_one = False

    # 是否全部种完
    if n == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    flowerbed = [1,0,0,0,0,0,1]
    print(canPlaceFlowers(flowerbed, 3))
