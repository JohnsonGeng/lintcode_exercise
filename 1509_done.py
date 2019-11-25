'''
问题描述：
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例：
输入：bills = [5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

思路：
其实只要记录5块、10块有多少张就可以了


'''


def lemonadeChange(bills):
    # Write your code here.
    # 思路：其实只要记录5块、10块有多少张就可以了
    five_dollar = 0
    ten_dollar = 0
    for bill in bills:
        # 如果是5块，那么不需要找零
        if bill == 5:
            five_dollar += 1
        # 如果是10块，需要找零5块
        elif bill == 10:
            if five_dollar >= 1:
                five_dollar -= 1
                ten_dollar += 1
            else:
                return False
        # 如果是20块，可以找零3张5块或者1张10块和1张5块
        else :
            # 一张10块和一张5块
            if ten_dollar >= 1 and five_dollar >= 1:
                ten_dollar -= 1
                five_dollar -= 1
            # 三张5块
            elif five_dollar >= 3:
                five_dollar -= 3
            else:
                return False
    return True


if __name__ == '__main__':
    bills = [5,5,5,10,20]
    print(lemonadeChange(bills))