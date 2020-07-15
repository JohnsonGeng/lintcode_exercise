'''

问题描述：
给定长度为偶数的整数数组，该数组中不同的数字代表不同种类的糖果，每个数字表示一种糖果。
您需要将这些糖果平均分配给弟弟和妹妹。 返回妹妹可以获得的糖果种类的最大数量。
所给数组的长度范围为[2, 10,000]，且为偶数。
所给数组中数字的范围为[-100,000, 100,000]。

示例：
Input : candies = [1,1,2,2,3,3]
Output : 3
Explanation :
有三种不同的糖果(1, 2 and 3), 每种糖果有两个。
最佳分法：妹妹拥有[1,2,3] ，弟弟也会拥有拥有[1,2,3]。
妹妹拥有3种不同的糖果。


'''


def distributeCandies(candies):
    # write your code here

    type_set = set()

    # 利用集合统计糖果的种类
    for ele in candies:
        type_set.add(ele)

    return int(min((len(candies) / 2), len(type_set)))